# Twilight API Documentation

<h1 style="font-size: 48px; font-weight: bold; vertical-align: middle;"><p align="center">
 <img src="source/images/image.avif" alt="Twilight Pool" width="32"> Twilight
</p></h1>

<p align="center">
  <strong>API reference for the Twilight Protocol stack</strong>
</p>

<p align="center">
  <a href="https://usmanshahid86.github.io/twilight-api-docs/">Read Full Documentation</a>
</p>

---

## Overview

This repository is the API reference for the Twilight Protocol stack. It documents the Nyks chain LCD endpoints, the zkOS privacy-layer RPC, and the Indexer API — providing developers with one place to discover and integrate with Twilight's APIs.

> **Looking for the Client SDK?** See the [twilight-rust-sdk](https://github.com/aspect-build/twilight-rust-sdk) repository.

### What is Twilight?

Twilight combines the security of distributed Bitcoin custody with advanced DeFi capabilities. Key properties include:

- **Always Inflight Bitcoin** — Your Bitcoin is constantly moving between validators, preventing any single party from claiming custody
- **Bitcoin-Derived Security** — Direct security inheritance from Bitcoin with inscribed exit hatches for permissionless fund recovery
- **Efficient Capital Requirements** — Secures $1B with only $10M in stake (100:1 ratio) through distributed trust assumptions
- **Distributed Signing** — All validators share signatures on the distributed ledger, eliminating centralized aggregation servers
- **Fast Confirmations** — 2-block deposit confirmation using validity gadgets for predictive finality

### API Layers

| Layer | Protocol | Description |
|-------|----------|-------------|
| **Nyks Chain** | REST (LCD) | Cosmos SDK–based blockchain. Endpoints for auth, bank, staking, governance, distribution, and Twilight-specific modules (bridge, fork, volt, zkOS protocol). |
| **zkOS RPC** | JSON-RPC 2.0 | Privacy layer. UTXO queries, shielded transfers, mint/burn operations, and encrypted account state. |
| **Indexer API** | REST + WebSocket | Read-only indexed chain data, full-text search, analytics, and real-time event streams. |

## API Endpoints

### Mainnet

| API | URL |
|-----|-----|
| Chain LCD | `https://lcd.twilight.org` |
| zkOS RPC | `https://nykschain.twilight.rest/zkos/` |
| Indexer REST | `https://indexer.twilight.org/api` |
| Indexer WebSocket | `wss://indexer.twilight.org/ws` |

### Testnet

| API | URL |
|-----|-----|
| Chain LCD | `https://lcd.twilight.rest` |

## Build & Deploy

This site is built with [Slate](https://github.com/slatedocs/slate) (Ruby / Middleman).

```bash
# Install dependencies
bundle install

# Local preview (port 4567)
bundle exec middleman server

# Build static site
bundle exec middleman build
```

Pushes to `main` trigger GitHub Pages deployment at `https://usmanshahid86.github.io/twilight-api-docs/`.

## Repository Structure

```
source/
├── index.html.md            # Landing page
├── chain.html.md            # Chain LCD entry point
├── zkos.html.md             # zkOS RPC entry point
├── indexer.html.md          # Indexer API entry point
├── reference.html.md        # Combined reference (all APIs)
└── includes/
    ├── _getting_started.md  # Quick-start guide
    ├── _conventions.md      # Shared conventions (errors, pagination, formats)
    ├── _chain_*.md          # Chain module docs (bridge, volt, fork, zkOS protocol, cosmos modules)
    ├── _zkos.md             # zkOS RPC methods
    ├── _indexer_api.md      # Indexer REST + WebSocket endpoints
    └── _indexer.md          # Indexer architecture overview
```

## Links

- **Live Docs**: [usmanshahid86.github.io/twilight-api-docs](https://usmanshahid86.github.io/twilight-api-docs/)
- **Protocol Docs**: [docs.twilight.org](https://docs.twilight.org)
- **Twilight Website**: [twilight.org](https://twilight.org)

---

<p align="center">
  <em>Built by the Twilight team</em>
</p>
