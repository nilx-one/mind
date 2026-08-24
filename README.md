# nilx.one mind

> Canonical durable organization and namespace context for `nilx.one`.

This repository is a concrete organization implementation of the implementation-independent [Mind Protocol](https://github.com/0x0sky/mind).

## Organization identity

- **Organization / namespace:** `nilx.one`
- **Canonical subject id:** `nilx-one`
- **GitHub namespace:** [`nilx-one`](https://github.com/nilx-one)
- **Parent organization:** [`aiaiaiai` / `4xAI`](https://github.com/aiaiaiai-org)
- **Owner / root identity:** [0x0sky](https://github.com/0x0sky)
- **Role:** protocol and ecosystem namespace

The canonical display name `nilx.one` is authored organization identity. `nilx-one` is the current GitHub namespace and also the protocol id chosen for this organization; provider metadata does not define or own that id.

`nilx.one` is not synonymous with `0x1`. `0x1` is a separate product identity whose canonical repository lives inside this namespace.

The parent-child and product relationships above are durable authored human context inherited from this repository's historical baseline documentation. This initial protocol canary deliberately does not invent machine relationship predicates for them.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. This is the first concrete `nilx.one` mind line:

- Mind Protocol: `0.9.0`;
- manifest schema: v3;
- organization context: `0.2.0`.

`protocol.lock.yaml` pins the exact immutable upstream `v0.9.0` tag and commit, protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set. Protocol version and organization context version are independent.

## Historical baseline

The branch `foundation/baseline-v0.1.0` remains immutable historical source material. It represented an abstract baseline without a concrete subject. `master` was created from that exact historical tip before this feature branch, so no prior authored history is discarded.

This `0.2.0` line is a fresh concrete publication, not a claim that baseline `0.1.0` is inside the supported protocol migration floor. Details are recorded in [`docs/migrations/foundation-to-mind-0.9.md`](docs/migrations/foundation-to-mind-0.9.md).

## Composition

```text
OrganizationMind
├── manifest.yaml
├── protocol.yaml
├── protocol.lock.yaml
├── conformance.yaml
├── compatibility.yaml
├── schema/
│   ├── protocol.schema.json
│   ├── mind.schema.json
│   ├── module.schema.json
│   ├── identity.schema.json
│   ├── identity-resource.schema.json
│   ├── relationships.schema.json
│   ├── visual-assets.schema.json
│   ├── conformance.schema.json
│   └── compatibility.schema.json
└── modules/
    └── identity/
```

## Canary boundary

The 0.9 synchronization is intentionally narrow:

- publish one universal organization Identity resource;
- pin the exact protocol release contract set;
- validate subject/owner binding and repository visibility;
- preserve `0x1` as a distinct product identity without importing it into this organization resource;
- do not infer relationships from GitHub metadata;
- do not require a final logo or provider binding;
- do not copy generic parent-organization content into this repository.

Full named visual-family, provider, product/project, and broader ecosystem enrichment remains a separate post-1.0 rollout.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
