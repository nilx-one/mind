# nilx.one mind

> Canonical durable organization and namespace context for `nilx.one`.

This repository is a standalone concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/aiaiaiai-org/mind-protocol).

## Organization identity

- **Organization / namespace:** `nilx.one`
- **Canonical subject id:** `nilx-one`
- **GitHub namespace:** [`nilx-one`](https://github.com/nilx-one)
- **Parent organization:** [`aiaiaiai` / `4xAI`](https://github.com/aiaiaiai-org)
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** protocol and ecosystem namespace

The canonical display name `nilx.one` is authored organization identity. `nilx-one` is the stable canonical id chosen for this organization and is also its current GitHub namespace; provider metadata does not define or own that id.

`nilx.one` is not synonymous with `0x1`. `0x1` remains a separate product identity whose canonical repository lives inside this namespace.

The parent-child and product relationships above are durable authored human context inherited from this repository's historical baseline documentation. This RC synchronization deliberately does not invent machine relationship predicates for them.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. This concrete `nilx.one` Mind currently publishes:

- Mind Protocol: `1.0.0-rc.2`;
- manifest schema: v3;
- organization context: `0.2.0`.

`mind-repository.yaml` declares this repository as a concrete Mind only. It is neither protocol authority nor template/reference authority. Its relationship to `aiaiaiai-org/mind-protocol` is `independent_consumer`.

Exact release provenance:

- authority/release repository: `aiaiaiai-org/mind-protocol`;
- tag: `v1.0.0-rc.2`;
- commit: `acdcedcf02c8b4ef314179bf54955a84606c8fb5`.

`protocol.lock.yaml` pins the exact protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set. The schema bytes remain the frozen pre-1.0 shapes; only the consumed release binding advances to the RC.

Protocol version and organization context version remain independent. Canonical Identity stays `organization:nilx-one` with display name `nilx.one`, while `mind.context_version` stays `0.2.0`.

## Historical baseline

The branch `foundation/baseline-v0.1.0` remains immutable historical source material. It represented an abstract baseline without a concrete subject. `master` was created from that exact historical tip before the 0.9 synchronization, so no prior authored history is discarded.

This `0.2.0` line remains the concrete organization context line. Details of the original bridge are recorded in [`docs/migrations/foundation-to-mind-0.9.md`](docs/migrations/foundation-to-mind-0.9.md).

## Composition

```text
OrganizationMind
├── manifest.yaml
├── mind-repository.yaml
├── protocol.yaml
├── protocol.lock.yaml
├── conformance.yaml
├── compatibility.yaml
├── schema/
└── modules/
    └── identity/
```

## Consumer boundary

This synchronization intentionally remains narrow:

- preserve one authored organization Identity resource;
- pin the exact immutable RC contract set;
- validate subject/owner binding and repository visibility;
- preserve `0x1` as a distinct product identity without importing it into this organization resource;
- do not infer relationships from GitHub metadata;
- do not require or invent a final visual identity;
- do not copy generic parent-organization content into this repository.

Protocol compatibility is expressed by the exact release lock, not GitHub fork ancestry. Full named visual-family, provider, product/project, and broader ecosystem enrichment remains post-`1.0.0` work.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
