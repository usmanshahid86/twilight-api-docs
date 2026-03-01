# Start Here

This section helps you choose the right API and get the network details you need.

## Which API Should I Use?

| Your goal | Use | Base URL |
|-----------|-----|----------|
| Query on-chain state (accounts, balances, staking, gov) | **Nyks Chain (LCD REST)** | `https://lcd.twilight.org` |
| Submit transactions, simulate gas, broadcast txs | **Nyks Chain (LCD REST)** | `https://lcd.twilight.org` |
| Privacy layer: UTXOs, shielded transfers, burn/mint | **zkOS RPC** | `https://nykschain.twilight.rest/zkos/` |
| Indexed data: blocks, tx history, search, analytics | **Indexer API** | `https://indexer.twilight.org/api` |
| Build wallets, trading apps, relayer integrations | **Client SDK** | Rust crate |

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
| **Query account balance** | LCD REST → `/cosmos/bank/v1beta1/balances/{address}` |
| **Build & broadcast a tx** | LCD REST → `/cosmos/tx/v1beta1/simulate`, `/cosmos/tx/v1beta1/txs` |
| **Get shielded UTXOs** | zkOS RPC → `getUtxos`, `getMemoUtxos`, `getStateUtxos` |
| **Submit private transfer** | zkOS RPC → `txCommit` |
| **Search blocks / txs by address** | Indexer API → `/api/blocks`, `/api/transactions`, `/api/search` |
| **Real-time block / tx events** | Indexer API → WebSocket |
| **Build a wallet or trading app** | Client SDK (Rust) |

## Quick Links

- [Nyks Chain API](#twilight-chain-api) — REST endpoints
- [zkOS RPC](#zkos-rpc-api) — Privacy layer
- [Indexer API](#indexer-api) — Indexed data & search
- [Client SDK](#twilight-client-sdk) — Rust SDK