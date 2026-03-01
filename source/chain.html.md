---
title: Nyks Chain API — Twilight Protocol
language_tabs:
  - shell
  - javascript
  - rust
toc_footers:
  - Twilight © 2025
includes:
  - chain_zkos_protocol
  - chain_twilight_bridge
  - chain_twilight_fork
  - chain_twilight-volt
  - chain_cosmos-auth
  - chain_cosmos-bank
  - chain_cosmos-distribution
  - chain_cosmos-gov
  - chain_cosmos-slashing
  - chain_cosmos-staking
  - chain_cosmos-tendermint
  - chain_cosmos-tx
  - chain_ibc
  - chain_misc-other
  - chain_tendermint
search: true
code_clipboard: true
meta:
  - name: description
    content: REST API reference for the Nyks/Twilight Chain — accounts, staking, governance, IBC, and more.
---

# Twilight Chain API

The Nyks Chain exposes a Cosmos SDK LCD (Light Client Daemon) REST API. Use it to query on-chain state, simulate and broadcast transactions, and interact with Twilight-specific modules (bridge, fork, volt, zkOS protocol). All endpoints follow REST conventions; no authentication required for public queries.

**Base URL:** `https://lcd.twilight.org`

---

**Navigate to another section:**
[Home](index.html) · [zkOS RPC](zkos.html) · [Indexer API](indexer.html) · [Client SDK](sdk.html) · [Full Reference](reference.html)
