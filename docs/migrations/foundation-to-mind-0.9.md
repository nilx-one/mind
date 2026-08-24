# Foundation baseline to Mind Protocol 0.9

This document records the first concrete `nilx.one` Mind publication from the repository's historical abstract baseline.

## Historical state

- historical baseline branch: `foundation/baseline-v0.1.0`
- baseline tip: `655c8e4c505ea1c26c3a79ec1a2f7afbf61190e5`
- baseline manifest schema: `1`
- baseline context version: `0.1.0`
- baseline subject: not concrete
- destination protocol: `0.9.0`
- destination manifest schema: `3`
- first concrete context version: `0.2.0`

The historical baseline is below Mind Protocol 0.9's supported `0.6.0` migration floor and has no concrete subject. This is a fresh concrete publication, not a supported automated migration from `0.1.0`.

## Branch preservation

The historical baseline branch is preserved untouched. A `master` branch was created from the exact baseline tip before `feature/mind-protocol-0.9-sync`, preserving all authored history without force rewriting the foundation branch.

Changing the repository default branch from `foundation/baseline-v0.1.0` to `master` is repository metadata, not protocol semantics. It remains a separate metadata action if the available GitHub integration cannot mutate that setting directly.

## Authored facts preserved

The historical README explicitly authored:

- organization / namespace display name `nilx.one`;
- GitHub namespace `nilx-one`;
- parent `aiaiaiai` ecosystem membership;
- root owner `0x0sky`;
- role as protocol and ecosystem namespace;
- `nilx.one` is not synonymous with `0x1`; `0x1` is a separate product identity in this namespace.

These facts remain human-readable organization context. This initial canary does not silently promote parent-child or product relationships into machine-readable relationship predicates.

## Protocol consumption

The concrete mind consumes the immutable `0x0sky/mind` release tag `v0.9.0` at commit `457844c8ced0318d91d628617ff6f8ec6f428ab7`.

`protocol.lock.yaml` records the exact protocol descriptor, conformance contract, compatibility policy, and complete frozen schema set with Git blob SHA-1 fingerprints. CI proves the local frozen schema descriptors match the published release compatibility freeze exactly.

Protocol tags are not created in this concrete repository. Protocol version and `nilx.one` context version remain independent.

## Concrete publication boundary

The first `0.2.0` line publishes only:

- manifest v3;
- subject and publication owner `organization:nilx-one`;
- display name `nilx.one`;
- one universal Identity resource;
- exact protocol-release machine contracts;
- public visibility boundaries;
- validation and CI.

It deliberately does not invent relationships, provider bindings, `0x1` product semantics, or canonical visual assets.

<!-- © 2026 aiaiaiai · aiaiaiai.org -->
