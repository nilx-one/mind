# Provider avatar projection

The canonical `nilx.one` identity mark lives in this repository as SVG. Provider surfaces consume a generated projection; they do not define the identity.

For GitHub, generate the square 1024×1024 white-canvas PNG with:

```sh
python scripts/export_visual_assets.py
```

The approved provider projection has SHA-256 `798604a59d9d533eb844393f2844504a6c1fd3317e65a713cf6e3d66f3389100` when produced with the pinned CI renderer dependency. Uploading that projection to GitHub is a manual provider action and is intentionally separate from merging the canonical Mind publication.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
