# Conventions

Common patterns across Twilight APIs.

## Pagination

| API | Parameters | Notes |
|-----|------------|-------|
| **LCD REST** | `pagination.key`, `pagination.limit`, `pagination.offset` | Use `key` for cursor-based; `offset` for page-based |
| **Indexer** | `page`, `limit` | Default `limit`: 20, max: 100 |

## Data Formats

- **BigInt**: Balances, gas amounts, and volumes are returned as **strings** in JSON.
- **Timestamps**: ISO 8601 format.
- **Addresses**: Bech32 with `twilight` prefix.

## Indexer vs LCD

| Use case | Prefer |
|----------|--------|
| Authoritative on-chain state | LCD REST |
| Historical queries, search, analytics | Indexer API |
| Real-time events (blocks, txs) | Indexer WebSocket |
| Transaction submission | LCD REST or zkOS RPC |