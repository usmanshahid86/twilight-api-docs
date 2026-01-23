# Twilight Relayer API Documentation

<h1 style="font-size: 48px; font-weight: bold; vertical-align: middle;"><p align="center">
 <img src="source/images/image.avif" alt="Twilight Pool" width="32"> Twilight
</p></h1>

<p align="center">
  <strong>Complete API documentation for Twilight's Relayer service</strong>
</p>

<p align="center">
  <a href="https://docs.twilight.rest">📖 Read Full Documentation</a>
</p>

---

## Overview

The Twilight Relayer API provides comprehensive access to decentralized trading, lending, and market data functionality built on Twilight's revolutionary Bitcoin reserve architecture. Twilight combines the security of distributed Bitcoin custody with the flexibility of twilight pools - Alternative Trading Systems that allow selective information revelation for sophisticated DeFi strategies.

### 🏦 What is Twilight?

Twilight serves as an antidote to rising walled gardens of centralized custody, maintaining Bitcoin's core value of distributed trust while providing advanced DeFi capabilities. Key properties include:

- **Always Inflight Bitcoin** - Your Bitcoin is constantly moving between validators, preventing any single party from claiming custody
- **Bitcoin-Derived Security** - Direct security inheritance from Bitcoin with inscribed exit hatches for permissionless fund recovery
- **Efficient Capital Requirements** - Secures $1B with only $10M in stake (100:1 ratio) through distributed trust assumptions
- **Distributed Signing** - All validators share signatures on the distributed ledger, eliminating centralized aggregation servers
- **Fast Confirmations** - 2-block deposit confirmation using validity gadgets for predictive finality

### 📡 API Categories

This documentation covers three main API categories:

- **Nyks API** - Chain Information
- **Zkos API** - Underlying privacy layer. Utxo related information 
- **Client SDK** - Information on interating with the Twilight protocol stack including the **Nyks chain**, **zkOS RPC layer**, and **App APIs(e.g., Exchange/Relayer)**,

## 🌐 API Endpoints

### Mainnet-beta

- **REST API**: `https://lcd.twilight.org`
- **WebSocket**: `wss://lcd.twilight.org/ws`

### Testnet

- **REST API**: `https://lcd.twilight.rest`
- **WebSocket**: `wss://lcd.twilight.rest/ws`

## 📚 Complete Documentation

**👉 [Visit docs.twilight.rest](https://docs.twilight.org/api) for the complete interactive API documentation**


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

## Zkos Privacy Layer 

ZkOS is a privacy-preserving blockchain infrastructure that powers Twilight's confidential transaction system. It provides a zero-knowledge enabled transaction layer that enables private value transfers, programmable data containers, and smart contract state management while maintaining transaction privacy.

### Key Capabilities

ZkOS enables:

- **Confidential Transactions** - Private value transfers using ElGamal encryption and zero-knowledge proofs, hiding transaction amounts and relationships
- **Privacy-Preserving State Management** - UTXO-based state management with immutability and efficient verification of state transitions
- **Programmable Privacy** - Time-bound data access controls and smart contract state
- **Cryptographic Proof Generation** - Range proofs, same-value proofs, and shuffle proofs to verify transactions without revealing sensitive information
- **Blockchain Integration** - Seamless integration with Cosmos-based blockchains through chain oracle services
- **RESTful API Access** - JSON-RPC interface for querying UTXO state, submitting transactions, and interacting with the privacy layer

ZkOS enhances the traditional privacy layers with the QuisQuis protocol, providing enhanced privacy guarantees that enable sophisticated DeFi strategies while maintaining confidentiality of user transactions and balances.

## 🔓 Chain API Features

The Chain API provides access to market data and general information without authentication:

### Available Endpoints


### Example: 



## 🔐 Zkos API Features

The Zkos API requires authentication and provides trading and account management functionality:

### Available Endpoints


### Example: 



## 🔄  Client SDK Features



###




## 🛠 Technical Details

### JSON-RPC Protocol

All APIs use JSON-RPC 2.0 protocol with the following structure:

```json
{
  "jsonrpc": "2.0",
  "method": "method_name",
  "id": 123,
  "params": {
    /* method parameters */
  }
}
```

### zkOS Integration

Private API endpoints utilize zkOS (Zero-Knowledge Operating System) for:

- **Privacy-preserving transactions**
- **Cryptographic proof generation**
- **Secure order execution**
- **Decentralized settlement**


## 🚀 Getting Started

1. **Explore Chain APIs** - Start with public endpoints to understand the data structure


## 📖 Full Documentation

This README provides a high-level overview. For complete API documentation including:

- **Detailed parameter specifications**
- **Response schemas and examples**
- **Authentication guides**
- **Error handling**
- **Rate limiting information**
- **SDK and integration examples**

**Visit: [https://docs.twilight.rest](https://docs.twilight.org/api)**

## 🔗 Links

- **API Documentation**: [docs.twilight.org/api](https://docs.twilight.org/api)
- **Protocol Documentation**: [docs.twilight.org](https://docs.twilight.org)
- **Twilight Protocol**: [twilight.org](https://twilight.org)
- **Support**: Contact through official channels

---

<p align="center">
  <em>Built with ❤️ by the Twilight team</em>
</p>
