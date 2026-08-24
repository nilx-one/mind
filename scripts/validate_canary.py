#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate the initial nilx.one Mind Protocol 0.9 canary boundary."""

from __future__ import annotations

import sys
from pathlib import Path

from validate_manifest import load_yaml_mapping

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ENTITY = {"type": "organization", "id": "nilx-one"}


def validate() -> list[str]:
    errors: list[str] = []
    manifest = load_yaml_mapping(ROOT / "manifest.yaml")
    mind = manifest.get("mind", {})

    if manifest.get("schema_version") != 3:
        errors.append("manifest schema_version must be 3")
    if manifest.get("protocol") != {"id": "mind", "version": "0.9.0"}:
        errors.append("manifest must consume Mind Protocol 0.9.0")
    if mind.get("name") != "mind@nilx-one":
        errors.append("canonical mind name must be mind@nilx-one")
    if mind.get("context_version") != "0.2.0":
        errors.append("first concrete context line must be 0.2.0")
    if mind.get("subject") != EXPECTED_ENTITY:
        errors.append("canonical subject must be organization:nilx-one")
    if mind.get("owner") != EXPECTED_ENTITY:
        errors.append("publication owner must be organization:nilx-one")
    if "kind" in mind:
        errors.append("mind.kind is forbidden by manifest v3")
    if "public_organizations" in manifest:
        errors.append("public_organizations is forbidden by manifest v3")

    modules = manifest.get("modules", {})
    if modules.get("required") != ["identity"]:
        errors.append("initial canary must require only the identity module")
    if modules.get("registered") != ["identity"]:
        errors.append("initial canary must register only the identity module")

    descriptor = load_yaml_mapping(ROOT / "modules/identity/module.yaml")
    if descriptor.get("module", {}).get("owner") != EXPECTED_ENTITY:
        errors.append("identity module owner must be organization:nilx-one")

    identity = load_yaml_mapping(ROOT / "modules/identity/identity.yaml").get("identity")
    if identity != {
        "type": "organization",
        "id": "nilx-one",
        "display_name": "nilx.one",
    }:
        errors.append("canonical Identity value is not the expected nilx.one organization")
    if isinstance(identity, dict) and "visual_identity" in identity:
        errors.append("initial 0.9 canary must not invent a canonical visual identity")

    if (ROOT / "modules/relationships/module.yaml").exists():
        errors.append("initial canary must not invent a relationship module")

    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, TypeError) as error:
        print(f"nilx.one canary validation failed:\n- {error}", file=sys.stderr)
        return 1

    if errors:
        print("nilx.one canary validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("nilx.one Mind Protocol 0.9 canary boundary is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
