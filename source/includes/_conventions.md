# Conventions

Common patterns across Twilight APIs.

## Authentication

No authentication is required for any public query endpoint across all three APIs (Chain LCD, zkOS RPC, Indexer).

## HTTP Methods

| API | Protocol | Methods |
|-----|----------|---------|
| **Chain LCD** | REST | `GET` for queries, `POST` for transaction broadcast/simulation |
| **zkOS RPC** | JSON-RPC 2.0 | All requests via `POST` |
| **Indexer** | REST | `GET` for queries |

## Pagination

| API | Parameters | Notes |
|-----|------------|-------|
| **LCD REST** | `pagination.key`, `pagination.limit`, `pagination.offset` | Use `key` for cursor-based; `offset` for page-based |
| **Indexer** | `page`, `limit` | Default `limit`: 20, max: 100 |

**LCD example:**

```shell
curl "https://lcd.twilight.org/cosmos/staking/v1beta1/validators?pagination.limit=10&pagination.offset=0"
```

**Indexer example:**

```shell
curl "https://indexer.twilight.org/api/blocks?page=1&limit=20"
```

## Data Formats

- **BigInt**: Balances, gas amounts, and volumes are returned as **strings** in JSON (e.g., `"1000000"` not `1000000`).
- **Timestamps**: ISO 8601 format (e.g., `"2025-01-15T12:30:00Z"`).
- **Addresses**: Bech32 with `twilight` prefix (e.g., `twilight1abc123...`).
- **Hex encoding**: zkOS RPC hex values do **not** include the `0x` prefix. Chain LCD hex values (e.g., `encryptScalar`) **do** include the `0x` prefix.

## Error Responses

**Chain LCD** returns Cosmos SDK errors:

```json
{
  "code": 3,
  "message": "invalid address: decoding bech32 failed",
  "details": []
}
```

**Indexer** returns JSON errors:

```json
{
  "error": "Resource not found"
}
```

**zkOS RPC** returns JSON-RPC 2.0 errors:

```json
{
  "jsonrpc": "2.0",
  "error": { "code": -32602, "message": "Invalid params" },
  "id": 1
}
```

## Rate Limiting

| API | Limit |
|-----|-------|
| **Indexer** | 100 requests per 60-second window |
| **Chain LCD** | No current limit |
| **zkOS RPC** | No current limit |

The Indexer returns `429 Too Many Requests` when the limit is exceeded. Retry after the window resets.

## Caching

Indexer responses include cache hints per endpoint (noted in each endpoint's documentation). Typical cache TTLs range from 2 seconds for blocks to 60 seconds for statistics.

## Indexer vs LCD

| Use case | Prefer |
|----------|--------|
| Authoritative on-chain state | LCD REST |
| Historical queries, search, analytics | Indexer API |
| Real-time events (blocks, txs) | Indexer WebSocket |
| Transaction submission | LCD REST or zkOS RPC |
