# Identity

Canonical public organization / namespace identity for `nilx.one`.

## Canonical identity

- **type:** organization
- **id:** `nilx-one`
- **display name:** `nilx.one`
- **GitHub namespace:** `github.com/nilx-one`

The machine-readable source is [`identity.yaml`](identity.yaml). Its type and id must match `manifest.yaml -> mind.subject` exactly.

The canonical display name is authored as `nilx.one`; the GitHub slug `nilx-one` is provider context. The protocol id remains provider-independent even where its current spelling matches a provider slug.

`nilx.one` is not synonymous with `0x1`. `0x1` is an independent product identity within this namespace and is deliberately outside this narrow organization Identity resource.

This concrete Mind currently consumes Mind Protocol `1.0.0-rc.2` and does not publish a canonical visual mark. Canonical visual identity remains optional and must be explicitly authored through a named visual-identity rollout; provider avatars and presentation fallbacks remain noncanonical unless deliberately adopted.

## Scope

This module owns only durable organization / namespace identity. Parent-child ecosystem relationships, product relationships, provider bindings, and runtime configuration require their own explicitly authored contracts and are not inferred here.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
