#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Generate and verify the provider-ready 1024px projection from the canonical SVG emblem."""

from __future__ import annotations

import argparse
import hashlib
import io
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SVG_PATH = ROOT / "assets" / "visual" / "nilx-one" / "compact-emblem.svg"
DEFAULT_OUTPUT = ROOT / "build" / "visual" / "nilx-one-compact-emblem-1024.png"
EXPECTED_VIEWBOX = (0.0, 0.0, 64.0, 64.0)
EXPECTED_FILL = "#7765C6"
EXPECTED_POINTS = ((10.0, 11.0), (24.0, 7.0), (40.0, 36.0), (40.0, 11.0), (54.0, 7.0), (52.0, 53.0), (40.0, 57.0), (24.0, 28.0), (24.0, 53.0), (10.0, 57.0))
EXPECTED_CHANNELS = ((10.5, 32.0, 24.0, 28.0), (27.0, 18.0, 38.0, 38.0), (40.0, 36.0, 53.0, 32.0))
EXPECTED_PNG_SHA256 = "798604a59d9d533eb844393f2844504a6c1fd3317e65a713cf6e3d66f3389100"
CANVAS = "#FFFFFF"
OUTPUT_SIZE = 1024
STROKE_WIDTH = 3.2


@dataclass(frozen=True)
class Line:
    x1: float
    y1: float
    x2: float
    y2: float


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_number_list(value: str) -> tuple[float, ...]:
    return tuple(float(part) for part in value.replace(",", " ").split())


def parse_svg() -> tuple[list[tuple[float, float]], list[Line], float]:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()
    namespace = {"svg": "http://www.w3.org/2000/svg"}

    viewbox = parse_number_list(root.attrib.get("viewBox", ""))
    if viewbox != EXPECTED_VIEWBOX:
        raise ValueError(f"unexpected viewBox: {viewbox!r}")

    polygon = root.find(".//svg:polygon[@id='mask-body']", namespace)
    channels = root.find(".//svg:g[@id='channels']", namespace)
    mark = root.find(".//svg:rect[@id='mark-fill']", namespace)
    if polygon is None or channels is None or mark is None:
        raise ValueError("canonical SVG is missing required controlled geometry")

    fill = mark.attrib.get("fill", "").upper()
    if fill != EXPECTED_FILL:
        raise ValueError(f"unexpected canonical fill: {fill!r}")

    points: list[tuple[float, float]] = []
    for raw in polygon.attrib.get("points", "").split():
        x, y = raw.split(",", maxsplit=1)
        points.append((float(x), float(y)))
    if tuple(points) != EXPECTED_POINTS:
        raise ValueError(f"canonical silhouette drifted: {tuple(points)!r}")

    stroke_width = float(channels.attrib.get("stroke-width", "0"))
    if stroke_width != STROKE_WIDTH:
        raise ValueError(f"unexpected channel width: {stroke_width!r}")

    lines: list[Line] = []
    for element in channels.findall("svg:line", namespace):
        lines.append(
            Line(
                x1=float(element.attrib["x1"]),
                y1=float(element.attrib["y1"]),
                x2=float(element.attrib["x2"]),
                y2=float(element.attrib["y2"]),
            )
        )
    actual_channels = tuple((line.x1, line.y1, line.x2, line.y2) for line in lines)
    if actual_channels != EXPECTED_CHANNELS:
        raise ValueError(f"canonical channel geometry drifted: {actual_channels!r}")
    return points, lines, stroke_width


def render_png_bytes() -> bytes:
    points, lines, stroke_width = parse_svg()
    scale = OUTPUT_SIZE / EXPECTED_VIEWBOX[2]
    image = Image.new("RGB", (OUTPUT_SIZE, OUTPUT_SIZE), CANVAS)
    draw = ImageDraw.Draw(image)
    draw.polygon([(round(x * scale), round(y * scale)) for x, y in points], fill=EXPECTED_FILL)

    width = round(stroke_width * scale)
    radius = width / 2
    for line in lines:
        start = (round(line.x1 * scale), round(line.y1 * scale))
        end = (round(line.x2 * scale), round(line.y2 * scale))
        draw.line((start, end), fill=CANVAS, width=width)
        for x, y in (start, end):
            draw.ellipse(
                (
                    round(x - radius),
                    round(y - radius),
                    round(x + radius),
                    round(y + radius),
                ),
                fill=CANVAS,
            )

    output = io.BytesIO()
    image.save(output, format="PNG", optimize=False, compress_level=9)
    return output.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify deterministic provider projection")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    try:
        data = render_png_bytes()
    except (OSError, ValueError, ET.ParseError) as error:
        print(f"provider projection generation failed: {error}", file=sys.stderr)
        return 1

    digest = sha256_bytes(data)
    if digest != EXPECTED_PNG_SHA256:
        print(
            f"provider projection drift: expected {EXPECTED_PNG_SHA256}, got {digest}",
            file=sys.stderr,
        )
        return 1

    if args.check:
        print(f"deterministic provider projection is current: sha256={digest}")
        return 0

    output_path = args.output
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)
    print(f"wrote {output_path} (sha256={digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
