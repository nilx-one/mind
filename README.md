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

The parent-child and product relationships above are durable authored human context inherited from this repository's historical baseline documentation. This protocol canary deliberately does not invent machine relationship predicates for them.

## Protocol contract

`manifest.yaml` is the machine-readable entry point. This concrete `nilx.one` Mind currently publishes:

- Mind Protocol: `0.9.0`;
- manifest schema: v3;
- organization context: `0.2.0`.

`mind-repository.yaml` declares this repository as a concrete Mind only. It is neither protocol authority nor template/reference authority. Its intended relationship to `aiaiaiai-org/mind-protocol` is an independent consumer, not GitHub fork inheritance.

`protocol.lock.yaml` keeps two facts separate:

- **current protocol authority:** `aiaiaiai-org/mind-protocol`;
- **immutable `0.9.0` release provenance:** `0x0sky/mind@v0.9.0`, commit `457844c8ced0318d91d628617ff6f8ec6f428ab7`.

The authority moved after `0.9.0`; that historical release is not recreated or rewritten in the new authority repository. Starting with `1.0.0-rc.1`, formal protocol releases are published from `aiaiaiai-org/mind-protocol`.

The lock pins the exact protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set. Protocol version and organization context version remain independent.

## Historical baseline

The branch `foundation/baseline-v0.1.0` remains immutable historical source material. It represented an abstract baseline without a concrete subject. `master` was created from that exact historical tip before the 0.9 synchronization, so no prior authored history is discarded.

This `0.2.0` line is a fresh concrete publication, not a claim that baseline `0.1.0` is inside the supported protocol migration floor. Details are recorded in [`docs/migrations/foundation-to-mind-0.9.md`](docs/migrations/foundation-to-mind-0.9.md).

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

Protocol compatibility is expressed by the exact release lock, not by GitHub fork ancestry. Full named visual-family, provider, product/project, and broader ecosystem enrichment remains a separate post-1.0 rollout.

## Visibility

This repository contains durable public organization context only. Never commit secrets, credentials, private personal data, private infrastructure state, or transient operational state.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
