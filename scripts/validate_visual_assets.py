#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate the canonical nilx.one visual-asset publication."""

from __future__ import annotations

import hashlib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from validate_manifest import load_schema, load_yaml_mapping, schema_errors

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "modules" / "identity" / "visual-assets.yaml"
IDENTITY_PATH = ROOT / "modules" / "identity" / "identity.yaml"
SCHEMA_PATH = ROOT / "schema" / "visual-assets.schema.json"
EXPECTED_REF = "nilx-one-compact-emblem"
EXPECTED_PATH = Path("assets/visual/nilx-one/compact-emblem.svg")
EXPECTED_SHA256 = "4d0c31dac359b577b142018ab96f40a5110bdd7d98e2e6beb8d34c8a9f273b15"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_path(relative_path: str) -> Path | None:
    root = ROOT.resolve()
    candidate = (ROOT / relative_path).resolve()
    if candidate != root and root not in candidate.parents:
        return None
    return candidate


def validate_descriptor(descriptor: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if descriptor.get("ref") != EXPECTED_REF:
        errors.append(f"asset ref must be {EXPECTED_REF!r}")
    if descriptor.get("media_type") != "image/svg+xml":
        errors.append("canonical primary mark must be image/svg+xml")
    if descriptor.get("resource_path") != EXPECTED_PATH.as_posix():
        errors.append(f"resource path must be {EXPECTED_PATH.as_posix()!r}")

    integrity = descriptor.get("integrity")
    if not isinstance(integrity, dict) or integrity.get("algorithm") != "sha256":
        errors.append("asset integrity must use sha256")
    elif integrity.get("digest") != EXPECTED_SHA256:
        errors.append("catalog digest drifted from the approved canonical SVG")

    path = safe_path(str(descriptor.get("resource_path", "")))
    if path is None or not path.is_file():
        errors.append("canonical SVG does not resolve inside the publication root")
        return errors
    if sha256(path) != EXPECTED_SHA256:
        errors.append("canonical SVG failed SHA-256 integrity validation")
        return errors

    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as error:
        errors.append(f"invalid canonical SVG: {error}")
        return errors
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        errors.append("canonical asset root must be SVG")
    if root.attrib.get("viewBox") != "0 0 64 64":
        errors.append("canonical compact emblem must use viewBox '0 0 64 64'")
    return errors


def validate_identity_binding(catalog: dict[str, Any]) -> list[str]:
    identity_resource = load_yaml_mapping(IDENTITY_PATH)
    identity = identity_resource.get("identity")
    if not isinstance(identity, dict):
        return ["identity resource is missing its embedded identity mapping"]
    visual_identity = identity.get("visual_identity")
    if not isinstance(visual_identity, dict):
        return ["identity.visual_identity must be authored"]
    primary_mark = visual_identity.get("primary_mark")
    if not isinstance(primary_mark, dict):
        return ["identity.visual_identity.primary_mark must be authored"]
    if primary_mark.get("kind") != "emblem":
        return ["identity.visual_identity.primary_mark.kind must be emblem"]
    if primary_mark.get("asset_ref") != EXPECTED_REF:
        return [f"primary mark asset_ref must be {EXPECTED_REF!r}"]
    matches = [
        asset for asset in catalog.get("assets", [])
        if isinstance(asset, dict) and asset.get("ref") == EXPECTED_REF
    ]
    if len(matches) != 1:
        return [f"primary mark must resolve exactly once; resolved {len(matches)} times"]
    return []


def main() -> int:
    errors: list[str] = []
    catalog = load_yaml_mapping(CATALOG_PATH)
    schema = load_schema(SCHEMA_PATH)
    errors.extend(
        f"catalog{error[1:]}"
        for error in schema_errors(Draft202012Validator(schema), catalog)
    )
    assets = catalog.get("assets")
    if not isinstance(assets, list) or len(assets) != 1 or not isinstance(assets[0], dict):
        errors.append("visual asset catalog must publish exactly one canonical source asset")
    elif not errors:
        errors.extend(validate_descriptor(assets[0]))
        errors.extend(validate_identity_binding(catalog))

    if errors:
        print("canonical visual asset validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "canonical nilx.one visual asset is valid: "
        f"{EXPECTED_REF} sha256={EXPECTED_SHA256}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
