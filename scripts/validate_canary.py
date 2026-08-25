#!/usr/bin/env python3
# © 2026 aiaiaiai · aiaiaiai.org
# SPDX-License-Identifier: MIT
"""Validate the nilx.one concrete Mind Protocol 1.0.0-rc.2 consumer boundary."""

from __future__ import annotations

import sys
from pathlib import Path

from validate_manifest import load_yaml_mapping

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ENTITY = {"type": "organization", "id": "nilx-one"}
EXPECTED_PROTOCOL_CONSUMPTION = {
    "id": "mind",
    "version": "1.0.0-rc.2",
    "authority_repository": "aiaiaiai-org/mind-protocol",
    "release_repository": "aiaiaiai-org/mind-protocol",
    "release_tag": "v1.0.0-rc.2",
    "release_commit": "acdcedcf02c8b4ef314179bf54955a84606c8fb5",
    "floating_master": "forbidden",
}


def validate() -> list[str]:
    errors: list[str] = []
    manifest = load_yaml_mapping(ROOT / "manifest.yaml")
    repository = load_yaml_mapping(ROOT / "mind-repository.yaml")
    mind = manifest.get("mind", {})

    if manifest.get("schema_version") != 3:
        errors.append("manifest schema_version must be 3")
    if manifest.get("protocol") != {"id": "mind", "version": "1.0.0-rc.2"}:
        errors.append("manifest must consume Mind Protocol 1.0.0-rc.2")
    if mind.get("name") != "mind@nilx-one":
        errors.append("canonical mind name must be mind@nilx-one")
    if mind.get("context_version") != "0.2.0":
        errors.append("protocol-only RC synchronization must preserve context_version 0.2.0")
    if mind.get("subject") != EXPECTED_ENTITY or mind.get("owner") != EXPECTED_ENTITY:
        errors.append("subject and publication owner must remain organization:nilx-one")

    roles = repository.get("repository", {}).get("roles", {})
    if roles.get("protocol_authority") != {"enabled": False}:
        errors.append("nilx-one/mind must not declare protocol authority")
    concrete = roles.get("concrete_mind", {})
    if concrete.get("enabled") is not True or concrete.get("canonical_for_subject") != EXPECTED_ENTITY:
        errors.append("repository must be a concrete Mind canonical only for organization:nilx-one")
    if concrete.get("reference_implementation") is not False or concrete.get("template_authority") is not False:
        errors.append("concrete organization Mind must not be reference or template authority")
    if repository.get("protocol_consumption") != EXPECTED_PROTOCOL_CONSUMPTION:
        errors.append("repository metadata must pin the immutable Protocol 1.0.0-rc.2 release exactly")
    if repository.get("fork_policy", {}).get("relationship_to_protocol_repository") != "independent_consumer":
        errors.append("protocol relationship must be independent_consumer")

    modules = manifest.get("modules", {})
    if modules.get("required") != ["identity"] or modules.get("registered") != ["identity"]:
        errors.append("RC consumer must contain only the authored identity module")

    descriptor = load_yaml_mapping(ROOT / "modules/identity/module.yaml")
    if descriptor.get("module", {}).get("owner") != EXPECTED_ENTITY:
        errors.append("identity module owner must be organization:nilx-one")

    identity = load_yaml_mapping(ROOT / "modules/identity/identity.yaml").get("identity")
    if identity != {"type": "organization", "id": "nilx-one", "display_name": "nilx.one"}:
        errors.append("canonical Identity must remain nilx.one / organization:nilx-one")
    if isinstance(identity, dict) and identity.get("id") == "0x1":
        errors.append("0x1 product identity must never replace the nilx.one organization Identity")
    if isinstance(identity, dict) and "visual_identity" in identity:
        errors.append("RC synchronization must not invent canonical visual identity")
    if (ROOT / "modules/relationships/module.yaml").exists():
        errors.append("RC synchronization must not invent a relationship module")

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
    print("nilx.one is a standalone concrete 1.0.0-rc.2 consumer with unchanged organization Identity/context")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
