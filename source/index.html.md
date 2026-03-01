---
title: Twilight Protocol API Reference
language_tabs:
  - shell
  - javascript
  - rust
toc_footers:
  - Twilight © 2025
includes:
  # === START HERE ===
  - getting_started          # Which API? Networks Quick links
  - conventions
  
  # === NYKS CHAIN (LCD REST) ===
  - chain_zkos_protocol      # Twilight zkOS module on chain  
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

  # === Zkos RPC ===
  - zkos

  # === INDEXER ===
  - indexer_api      # REST API (primary for developers)
  - indexer          # Service architecture (for operators)

  # === CLIENT SDK ===
  - sdk
code_clipboard: true
search: true
meta:
  - name: description
    content: Documentation for the Twilight protocol API
---

# Introduction

Welcome to the Twilight Protocol API documentation. This guide helps you integrate with the Nyks chain, zkOS privacy layer, Indexer, and Client SDK.

**New to Twilight?** Start with [Which API Should I Use?](#which-api-should-i-use) to pick the right interface for your use case, then jump to the relevant API reference.

**Quick navigation:**
- [Start Here](#start-here) — Chain info, networks, API decision table
- [Conventions](#conventions) — Pagination, data formats, common patterns
- [Nyks Chain API](#twilight-chain-api) — REST endpoints for on-chain state
- [zkOS RPC](#zkos-rpc-api) — Privacy layer (UTXOs, shielded transfers)
- [Indexer API](#indexer-api) — Indexed data, search, WebSocket
- [Client SDK](#twilight-client-sdk) — Rust SDK for wallets and apps