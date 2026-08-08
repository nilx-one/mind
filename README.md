# nilx.one mind

> A versioned organization and namespace context repository for humans and AI systems.

## Organization identity

- **Organization / namespace:** `nilx.one` (`nilx-one` on GitHub)
- **Parent organization:** [aiaiaiai tech. / 4xAI tech.](https://github.com/aiaiaiaitech)
- **Owner:** [0x0sky](https://github.com/0x0sky)
- **Role:** protocol and ecosystem namespace

`nilx.one` is a child organization / namespace in the aiaiaiai tech. ecosystem. This relationship belongs to the canonical organizational and ownership model; GitHub itself represents both organizations as peer namespaces.

`nilx.one` is not synonymous with `0x1`. `0x1` is a protocol product whose canonical repository lives inside this namespace.

## Purpose

This repository specializes the shared `mind` contract as durable context for the `nilx.one` organization / namespace. It records stable identity, ownership, parent relationship, ecosystem boundaries, and product relationships without duplicating repository-local implementation details.

## Ecosystem relationship

```text
0x0sky
└── aiaiaiai tech. / 4xAI tech.
    ├── 0xda-market
    └── nilx.one
        └── 0x1
```

Personal projects remain outside this corporate hierarchy unless explicitly declared otherwise.

## Contract

Every compatible mind must:

- declare an explicit owner and context version;
- keep one canonical location for each concept;
- separate stable context from transient state;
- keep modules focused and independently replaceable;
- declare module dependencies explicitly;
- prefer references over duplicated content;
- remain readable by humans and machines;
- contain no secrets or private credentials.

## Architecture

```text
Mind
├── manifest.yaml
├── schema/
│   └── mind.schema.json
└── modules/
    └── README.md
```

`Mind` is the shared abstraction. This repository is the `nilx.one` specialization of that abstraction.

## Design principles

- **Single Responsibility:** one purpose per module and one topic per file.
- **Open/Closed:** new mind types are added through modules, not by changing the baseline contract.
- **Interface Segregation:** consumers load only the modules they need.
- **Dependency Inversion:** concrete modules depend on the baseline contract; the baseline never depends on concrete modules.
- Composition is preferred over inheritance.
- Contracts are preferred over conventions that cannot be validated.

## Lifecycle

1. Track the shared mind contract explicitly.
2. Evolve this organization / namespace mind independently.
3. Keep parent, owner, and product relationships durable and visible.
4. Share neutral improvements upstream only through explicit commits or versioned specifications.

## Visibility

This repository may be public. Never commit secrets, credentials, private health data, access tokens, or other sensitive material.
