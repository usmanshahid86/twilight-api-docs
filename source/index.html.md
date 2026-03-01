---
title: Twilight Protocol API Documentation
language_tabs: []
toc_footers:
  - Twilight © 2025
search: true
code_clipboard: false
meta:
  - name: description
    content: Developer documentation for the Twilight Protocol — Nyks Chain API, zkOS RPC, Indexer API, and Client SDK.
---

# Twilight Protocol

Welcome to the Twilight Protocol developer documentation. Twilight is a privacy-preserving Bitcoin DeFi protocol built on the Nyks Cosmos SDK chain.

## Which API Should I Use?

| Your goal | Use | Link |
|-----------|-----|------|
| Query on-chain state (accounts, balances, staking, gov) | **Nyks Chain API** | [Chain API](chain.html) |
| Submit or simulate transactions, broadcast txs | **Nyks Chain API** | [Chain API](chain.html) |
| Privacy layer: UTXOs, shielded transfers, burn/mint | **zkOS RPC** | [zkOS RPC](zkos.html) |
| Indexed data: blocks, tx history, search, analytics | **Indexer API** | [Indexer API](indexer.html) |
| Build wallets, trading apps, relayer integrations | **Client SDK** | [Client SDK](sdk.html) |
| Browse everything in one page | **Full Reference** | [Full Reference](reference.html) |

## Section Guides

### [Nyks Chain API →](chain.html)

REST endpoints served by the LCD (Light Client Daemon). Query accounts, balances, staking state, governance proposals, IBC channels, and Twilight-specific modules.

**Base URL:** `https://lcd.twilight.org`

---

### [zkOS RPC →](zkos.html)

Zero-knowledge privacy layer. Manage UTXOs, submit shielded transfers, and interact with the proof system.

**Base URL:** `https://nykschain.twilight.rest/zkos/`

---

### [Indexer API →](indexer.html)

Read-only REST + WebSocket API for indexed chain data. Search blocks, transactions, accounts, validators, and BTC bridge operations.

**Base URL:** `https://indexer.twilight.org/api`

---

### [Client SDK →](sdk.html)

Rust crate that wraps all APIs into a high-level interface. The recommended starting point for building wallets and applications.

---

### [Full Reference →](reference.html)

All sections combined in a single scrollable page with unified sidebar and search.