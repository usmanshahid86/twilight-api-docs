# Start Here

Twilight is a privacy-preserving Bitcoin DeFi protocol built on the Nyks chain (Cosmos SDK). It provides distributed Bitcoin custody, zero-knowledge privacy transfers, and an indexed data layer for querying historical chain activity.

This section helps you choose the right API and get the network details you need.

## Prerequisites

All API endpoints are public and require no authentication. You only need an HTTP client (`curl`, `fetch`, etc.) to get started.

Quick test:

```shell
curl https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/node_info
```

## Which API Should I Use?

| Your goal | Use | Base URL |
|-----------|-----|----------|
| Query on-chain state (accounts, balances, staking, gov) | **Nyks Chain (LCD REST)** | `https://lcd.twilight.org` |
| Submit transactions, simulate gas, broadcast txs | **Nyks Chain (LCD REST)** | `https://lcd.twilight.org` |
| Privacy layer: UTXOs, shielded transfers, burn/mint | **zkOS RPC** | `https://nykschain.twilight.rest/zkos/` |
| Indexed data: blocks, tx history, search, analytics | **Indexer API** | `https://indexer.twilight.org/api` |
| Build wallets, trading apps, relayer integrations | **Client SDK** (external) | [SDK repo](https://github.com/AhmadAshraf2/zkos-client-wallet) |

## Chain Info

| Property | Mainnet | Testnet |
|----------|---------|---------|
| **Chain ID** | nyks | nyks-testnet |
| **Bech32 prefix** | twilight | twilight |
| **Denom** | NYKS, SATS | NYKS, SATS |

## Networks & Endpoints

| Network | LCD | Indexer | zkOS |
|---------|-----|---------|------|
| **Mainnet** | lcd.twilight.org | indexer.twilight.org | nykschain.twilight.rest/zkos |
| **Testnet** | lcd.twilight.rest | (if available) | nykschain.twilight.rest/zkos |

## Typical Developer Workflows

| Workflow | APIs used |
|----------|-----------|
| **Query account balance** | LCD REST → `GET /cosmos/bank/v1beta1/balances/{address}` |
| **Build & broadcast a tx** | LCD REST → `POST /cosmos/tx/v1beta1/simulate`, `POST /cosmos/tx/v1beta1/txs` |
| **Get shielded UTXOs** | zkOS RPC → `getUtxos`, `getMemoUtxos`, `getStateUtxos` |
| **Submit private transfer** | zkOS RPC → `txCommit` |
| **Search blocks / txs by address** | Indexer API → `GET /api/blocks`, `GET /api/transactions`, `GET /api/search` |
| **Real-time block / tx events** | Indexer WebSocket → `wss://indexer.twilight.org` |
| **Build a wallet or trading app** | [Client SDK](https://github.com/AhmadAshraf2/zkos-client-wallet) (Rust) |

## Quick Links

- [Nyks Chain API](#twilight-chain-api) — REST endpoints
- [zkOS RPC](#zkos-rpc-api) — Privacy layer
- [Indexer API](#indexer-api) — Indexed data & search
- [Client SDK](https://github.com/AhmadAshraf2/zkos-client-wallet) — Rust SDK (external repo)
