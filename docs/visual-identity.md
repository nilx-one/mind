# Canonical visual identity

`nilx-one/mind` is the canonical publication source for the `nilx.one` compact emblem.

The universal Mind Protocol defines only the semantics of `identity.visual_identity.primary_mark` and visual-asset resolution. This concrete Mind owns the named mark, its exact bytes, its SHA-256 integrity, and the independent organization context version that introduces it.

## Source of truth

- canonical identity: `modules/identity/identity.yaml`;
- asset catalog: `modules/identity/visual-assets.yaml`;
- canonical SVG: `assets/visual/nilx-one/compact-emblem.svg`;
- deterministic provider projection: `python scripts/export_visual_assets.py`.

The SVG uses the established `#7765C6` identity violet. Its faceted `N` belongs to the `nilx.one` organization/namespace and must not be reused as the canonical identity of the separate `0x1` product. Provider projection uses a white 1024×1024 canvas. GitHub avatars and other provider copies are downstream projections and never become identity authority.

## Integrity

`python scripts/validate_visual_assets.py` validates the catalog, canonical binding, controlled SVG path and SHA-256 digest. `python scripts/export_visual_assets.py --check` verifies that the controlled SVG geometry still produces the approved provider-ready PNG bytes.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
