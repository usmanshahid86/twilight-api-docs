# Twilight API Documentation

<h1 style="font-size: 48px; font-weight: bold; vertical-align: middle;"><p align="center">
 <img src="source/images/image.avif" alt="Twilight Pool" width="32"> Twilight
</p></h1>

<p align="center">
  <strong>Central API documentation for the Twilight Protocol stack</strong>
</p>

<p align="center">
  <a href="https://docs.twilight.rest">📖 Read Full Documentation</a>
</p>

---

## Overview

This repository is the single source of truth for all API documentation across the Twilight Protocol stack. It documents the Nyks chain, zkOS privacy layer, Client SDK, and related services—providing developers with one place to discover and integrate with Twilight's APIs.

### 🏦 What is Twilight?

Twilight combines the security of distributed Bitcoin custody with advanced DeFi capabilities. Key properties include:

- **Always Inflight Bitcoin** - Your Bitcoin is constantly moving between validators, preventing any single party from claiming custody
- **Bitcoin-Derived Security** - Direct security inheritance from Bitcoin with inscribed exit hatches for permissionless fund recovery
- **Efficient Capital Requirements** - Secures $1B with only $10M in stake (100:1 ratio) through distributed trust assumptions
- **Distributed Signing** - All validators share signatures on the distributed ledger, eliminating centralized aggregation servers
- **Fast Confirmations** - 2-block deposit confirmation using validity gadgets for predictive finality

### 📡 Documentation Layers

This documentation covers the Twilight Protocol stack:

| Layer | Description |
|-------|-------------|
| **Nyks Chain** | Cosmos SDK–based blockchain. REST APIs for auth, bank, staking, gov, distribution, and Twilight-specific modules (bridge, fork, volt, zkOS protocol). |
| **zkOS** | Privacy layer. JSON-RPC for UTXO queries, transaction submission, and encrypted account state. |
| **Client SDK** | Rust SDK for building apps that interact with the Nyks chain, zkOS RPC, and app APIs (e.g., Exchange/Relayer). |
| **Indexer API** | Read-only REST + WebSocket API for indexed chain data, search, and analytics. |


## 🌐 API Endpoints

### Mainnet

- **REST API**: `https://lcd.twilight.org`
- **WebSocket**: `wss://lcd.twilight.org/ws`

### Testnet

- **REST API**: `https://lcd.twilight.rest`
- **WebSocket**: `wss://lcd.twilight.rest/ws`

## 📚 Complete Documentation

**👉 [Visit docs.twilight.rest](https://docs.twilight.rest) for the complete interactive API documentation**

- **Production (main)**: [docs.twilight.rest](https://docs.twilight.rest)
- **Development (dev)**: [docs.twilight.rest/dev](https://docs.twilight.rest/dev)


## 🪃 Boomerang Protocol

The Boomerang protocol is Twilight's core innovation for maintaining distributed Bitcoin custody:

- **Bitcoin Fragments** - Your Bitcoin is split into fragments that continuously move between validators
- **Fragment Addresses** - Each fragment has unique addressing for tracking and verification
- **Automatic Sweeping** - Fragments are automatically swept and redistributed to prevent centralization
- **Clearing Mechanism** - Efficient settlement of trades and positions across the distributed network
- **Refund Snapshots** - Regular snapshots ensure funds can always be recovered

## 🕒 Validity Gadget

Twilight's Validity Gadget provides predictive finality and enhanced security:

- **Chaintip Attestation** - Validators attest to Bitcoin blockchain state for faster confirmations
- **2-Block Confirmation** - Achieve deposit confirmation in just 2 blocks instead of traditional 100+ blocks
- **Predictive Finality** - Advanced algorithms predict transaction finality on the longest chain
- **Liveness Guarantees** - Ensures the system remains operational even with validator failures

## 🔐 Security Model

Twilight's unique security approach:

- **1-of-n Trust Assumption** - System operates securely even if only one honest validator exists
- **n-of-n Malicious Resistance** - Designed to handle scenarios where all validators turn malicious
- **Inscribed Exit Hatches** - Bitcoin-native exit mechanisms that can be triggered permissionlessly
- **Distributed Validation** - No single point of failure in the validation process

## 💰 Capital Efficiency

- **100:1 Security Ratio** - Secure $1B in Bitcoin with only $10M in validator stake
- **Minimal Collateral Requirements** - Efficient capital utilization compared to traditional systems
- **Dynamic Stake Adjustment** - Validator stakes adjust based on network conditions and security needs

## ZkOS Privacy Layer

ZkOS is a privacy-preserving blockchain infrastructure that powers Twilight's confidential transaction system. It provides a zero-knowledge enabled transaction layer for private value transfers, programmable data containers, and smart contract state management.

### Key Capabilities

- **Confidential Transactions** - Private value transfers using ElGamal encryption and zero-knowledge proofs
- **Privacy-Preserving State Management** - UTXO-based state with immutability and efficient verification
- **Programmable Privacy** - Time-bound data access controls and smart contract state
- **Cryptographic Proof Generation** - Range proofs, same-value proofs, and shuffle proofs
- **Blockchain Integration** - Integration with Cosmos-based blockchains through chain oracle services
- **JSON-RPC Interface** - Query UTXO state, submit transactions, and interact with the privacy layer

## 🛠 Technical Details

### Build & Deploy

- **Build**: `bundle exec middleman build`
- **Local preview**: `bundle exec middleman server` (port 4567)
- **Deploy**: Pushes to `main` and `dev` trigger GitHub Actions; `main` deploys to the root, `dev` to `/dev`

### JSON-RPC (zkOS)

zkOS uses JSON-RPC 2.0:

```json
{
  "jsonrpc": "2.0",
  "method": "method_name",
  "id": 123,
  "params": { }
}
```

## 🚀 Getting Started

1. **Nyks Chain** - Use REST endpoints for chain data (auth, bank, staking, etc.)
2. **zkOS** - Use JSON-RPC for UTXO queries and transaction submission
3. **Client SDK** - Use the Rust SDK for wallet, trading, and relayer integration

## 📖 Full Documentation

For complete API documentation including parameter specifications, response schemas, examples, and SDK guides:

**Visit: [https://docs.twilight.rest](https://docs.twilight.rest)**

## 🔗 Links

- **API Documentation**: [docs.twilight.rest](https://docs.twilight.rest)
- **Protocol Documentation**: [docs.twilight.org](https://docs.twilight.org)
- **Twilight Protocol**: [twilight.org](https://twilight.org)
- **Support**: Contact through official channels

---

<p align="center">
  <em>Built by the Twilight team</em>
</p>
