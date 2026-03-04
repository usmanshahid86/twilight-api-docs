# Indexer Architecture

The **Nyks Chain Indexer** is a background service that syncs the Nyks blockchain into PostgreSQL. It processes blocks from the LCD API, decodes 23 custom module message types across 4 modules (bridge, forks, volt, zkOS), and publishes real-time events via Redis pub/sub for WebSocket delivery.

```
Nyks Chain (LCD API)
       |
       v
  Sync Loop ──> PostgreSQL <── API Server
       |              ^
       |              |
       +──> Redis ────+──> WebSocket
       |
  Enrichment Worker ──> zkOS Decode API
```

For the full indexer architecture, configuration, database schema, and deployment guide, see the [twilight-indexer-api repository](https://github.com/AhmadAshraf2/twilight-indexer-api).
