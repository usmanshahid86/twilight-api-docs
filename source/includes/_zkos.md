# Zkos RPC API

## Overview

The zkOS RPC API exposes the UTXO-based account state and encrypted account details tracked by the zkOS node. Use it to submit shielded transactions, query UTXOs and outputs, and interact with the zero-knowledge privacy layer.

**Base URL:** `https://nykschain.twilight.rest/zkos/`

**Development URL:** `http://localhost:3030/` (Local development)

> No authentication required. All requests use JSON-RPC 2.0 via HTTP POST.

---

## Parameter Formats

Methods accept parameters in two formats:

- **Positional (array):** Methods like `getUtxos`, `getOutput`, `txCommit` accept a JSON array of positional parameters.
- **Named (object):** Methods like `get_utxos_id`, `get_utxos_detail`, `getUtxosFromDB` accept a JSON object with named fields.

Check each endpoint's parameter table for the correct format.

> All hex-encoded values should be valid hexadecimal **without** the `0x` prefix.

---

## Error Responses

All errors follow the JSON-RPC 2.0 error format:

```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32602,
    "message": "Invalid params: expected hex-encoded address"
  },
  "id": 1
}
```

| Code | Meaning |
|------|---------|
| -32700 | Parse error — invalid JSON |
| -32600 | Invalid request — missing required fields |
| -32601 | Method not found |
| -32602 | Invalid params — wrong type or format |
| -32603 | Internal error — server-side failure |

---

## Table of Contents
1. [Transaction Operations](#transaction-operations)
2. [UTXO Queries](#utxo-queries)
3. [Output Queries](#output-queries)
4. [Database Queries](#database-queries)

---

## Transaction Operations

### Submit Transaction

```shell
# Transfer/Script Transaction
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "txCommit",
    "params": ["your_hex_encoded_transaction_here"],
    "id": 1
  }'

# Message Transaction (Burn) - requires twilight address as second parameter
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "txCommit",
    "params": ["your_hex_encoded_message_transaction_here", "twilight_address_here"],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'txCommit',
    params: ['your_hex_encoded_transaction_here'],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "tx_hash": "A1B2C3D4E5F6789012345678901234567890ABCDEF",
    "status": "success"
  },
  "id": 1
}
```

Commits a transaction to the blockchain with cryptographic verification and UTXO state updates. For message transactions with burn type, a twilight address must be provided as the second parameter.

### HTTP Method

`POST`

### RPC Method

`txCommit`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| [0] | string | Yes | Hex-encoded transaction data |
| [1] | string | **Conditional** | Twilight address (required ONLY for message transactions with burn type) |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| tx_hash | string | Transaction hash for blockchain confirmation |
| status | string | Transaction status ("success" or "failed") |

---

## UTXO Queries

### Get UTXOs by Address

Use `getUtxos` for coin UTXOs associated with a specific address. For all coin UTXOs system-wide, use `allCoinUtxos`.

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "getUtxos",
    "params": ["hex_encoded_zkos_account_address"],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'getUtxos',
    params: ['hex_encoded_zkos_account_address'],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "utxo_key": "a1b2c3d4e5f67890abcdef1234567890abcdef12...",
      "block_height": 12345
    }
  ],
  "id": 1
}
```

Retrieves coin-type UTXOs for a specific address.

### HTTP Method

`POST`

### RPC Method

`getUtxos`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| [0] | string | Yes | Hex-encoded address to query UTXOs for |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| utxo_key | string | Unique identifier for the UTXO |
| block_height | integer | Block height when UTXO was created |

---

### Get Memo UTXOs by Address

Use `getMemoUtxos` for memo UTXOs associated with a specific address. For all memo UTXOs system-wide, use `allMemoUtxos`.

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "getMemoUtxos",
    "params": ["hex_encoded_zkos_account_address"],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'getMemoUtxos',
    params: ['hex_encoded_zkos_account_address'],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "utxo_key": "b2c3d4e5f67890abcdef1234567890abcdef1234...",
      "memo_data": "encrypted_memo_content",
      "block_height": 12346
    }
  ],
  "id": 1
}
```

Retrieves memo-type UTXOs containing encrypted message data for a specific address.

### HTTP Method

`POST`

### RPC Method

`getMemoUtxos`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| [0] | string | Yes | Hex-encoded address to query memo UTXOs for |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| utxo_key | string | Unique identifier for the memo UTXO |
| memo_data | string | Encrypted memo content |
| block_height | integer | Block height when memo UTXO was created |

---

### Get State UTXOs by Address

Use `getStateUtxos` for state UTXOs associated with a specific address. For all state UTXOs system-wide, use `allStateUtxos`.

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "getStateUtxos",
    "params": ["hex_encoded_zkos_account_address"],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'getStateUtxos',
    params: ['hex_encoded_zkos_account_address'],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "utxo_key": "c3d4e5f67890abcdef1234567890abcdef123456...",
      "state_data": "encrypted_state_content",
      "block_height": 12347
    }
  ],
  "id": 1
}
```

Retrieves state-type UTXOs containing smart contract state data for a specific address.

### HTTP Method

`POST`

### RPC Method

`getStateUtxos`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| [0] | string | Yes | Hex-encoded address to query state UTXOs for |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| utxo_key | string | Unique identifier for the state UTXO |
| state_data | string | Encrypted state content |
| block_height | integer | Block height when state UTXO was created |

---

### Get All Coin UTXOs

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "allCoinUtxos",
    "params": [],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'allCoinUtxos',
    params: [],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "utxo_key": "d4e5f67890abcdef1234567890abcdef12345678...",
      "block_height": 12348
    }
  ],
  "id": 1
}
```

Retrieves all coin-type UTXOs in the system.

### HTTP Method

`POST`

### RPC Method

`allCoinUtxos`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| N/A | null | No | No parameters required |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| utxo_key | string | Unique identifier for the UTXO |
| block_height | integer | Block height when UTXO was created |

---

### Get All Memo UTXOs

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "allMemoUtxos",
    "params": [],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'allMemoUtxos',
    params: [],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "utxo_key": "e5f67890abcdef1234567890abcdef1234567890...",
      "memo_data": "encrypted_memo_content",
      "block_height": 12349
    }
  ],
  "id": 1
}
```

Retrieves all memo-type UTXOs in the system.

### HTTP Method

`POST`

### RPC Method

`allMemoUtxos`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| N/A | null | No | No parameters required |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| utxo_key | string | Unique identifier for the memo UTXO |
| memo_data | string | Encrypted memo content |
| block_height | integer | Block height when memo UTXO was created |

---

### Get All State UTXOs

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "allStateUtxos",
    "params": [],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'allStateUtxos',
    params: [],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "utxo_key": "f67890abcdef1234567890abcdef123456789012...",
      "state_data": "encrypted_state_content",
      "block_height": 12350
    }
  ],
  "id": 1
}
```

Retrieves all state-type UTXOs in the system.

### HTTP Method

`POST`

### RPC Method

`allStateUtxos`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| N/A | null | No | No parameters required |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| utxo_key | string | Unique identifier for the state UTXO |
| state_data | string | Encrypted state content |
| block_height | integer | Block height when state UTXO was created |

---

### Get UTXO IDs by Address

This method uses **named parameters** (object) instead of positional parameters (array).

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "get_utxos_id",
    "params": {
      "address_or_id": "hex_encoded_address",
      "input_type": "Coin"
    },
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'get_utxos_id',
    params: {
      address_or_id: 'hex_encoded_address',
      input_type: 'Coin'
    },
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": "hex_encoded_utxo_id",
  "id": 1
}
```

Retrieves UTXO IDs associated with a specific address and input type.

### HTTP Method

`POST`

### RPC Method

`get_utxos_id`

### Message Parameters

| Field | Data_Type | Required | Values |
| ----- | --------- | -------- | ------ |
| address_or_id | string | Yes | Hex-encoded address to query |
| input_type | string | Yes | UTXO type: `"Coin"`, `"Memo"`, or `"State"` |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| result | string | Hex-encoded UTXO ID |

---

### Get UTXO Details by Address

This method uses **named parameters** (object) instead of positional parameters (array).

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "get_utxos_detail",
    "params": {
      "address_or_id": "hex_encoded_address",
      "input_type": "Coin"
    },
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'get_utxos_detail',
    params: {
      address_or_id: 'hex_encoded_address',
      input_type: 'Coin'
    },
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "id": {
      "commitment": "hex_encoded_commitment",
      "nullifier": "hex_encoded_nullifier"
    },
    "output": {
      "value": "encrypted_value",
      "data": "encrypted_output_data"
    }
  },
  "id": 1
}
```

Retrieves comprehensive UTXO information including both the UTXO ID and associated output data.

### HTTP Method

`POST`

### RPC Method

`get_utxos_detail`

### Message Parameters

| Field | Data_Type | Required | Values |
| ----- | --------- | -------- | ------ |
| address_or_id | string | Yes | Hex-encoded address to query |
| input_type | string | Yes | UTXO type: `"Coin"`, `"Memo"`, or `"State"` |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| id | object | UTXO object containing commitment and nullifier data |
| output | object | Output object containing encrypted transaction data |

---

### Get Output by UTXO Key (Structured)

This method uses **named parameters** (object) instead of positional parameters (array).

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "get_output",
    "params": {
      "address_or_id": "hex_encoded_utxo_key",
      "input_type": "Coin"
    },
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'get_output',
    params: {
      address_or_id: 'hex_encoded_utxo_key',
      input_type: 'Coin'
    },
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "value": "encrypted_output_value",
    "data": "encrypted_output_data",
    "commitment": "hex_encoded_commitment"
  },
  "id": 1
}
```

Retrieves output data by UTXO key using structured parameters with explicit type specification.

### HTTP Method

`POST`

### RPC Method

`get_output`

### Message Parameters

| Field | Data_Type | Required | Values |
| ----- | --------- | -------- | ------ |
| address_or_id | string | Yes | Hex-encoded UTXO key to query |
| input_type | string | Yes | UTXO type: `"Coin"`, `"Memo"`, or `"State"` |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| value | string | Encrypted output value |
| data | string | Encrypted output data |
| commitment | string | Hex-encoded commitment for the output |

---

## Output Queries

### Get All Coin Outputs

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "allOutputs",
    "params": [],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'allOutputs',
    params: [],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "output_key": "7890abcdef1234567890abcdef12345678901234...",
      "value": "1000000",
      "block_height": 12351
    }
  ],
  "id": 1
}
```

Retrieves all coin-type outputs in the system.

### HTTP Method

`POST`

### RPC Method

`allOutputs`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| N/A | null | No | No parameters required |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| output_key | string | Unique identifier for the output |
| value | string | Output value in base currency units |
| block_height | integer | Block height when output was created |

---

### Get Specific Coin Output

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "getOutput",
    "params": ["hex_encoded_utxo_key"],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'getOutput',
    params: ['hex_encoded_utxo_key'],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "output_key": "90abcdef1234567890abcdef123456789012abcd...",
    "value": "1000000",
    "block_height": 12352,
    "transaction_hash": "abcdef1234567890abcdef1234567890abcdef12..."
  },
  "id": 1
}
```

Retrieves a specific coin output by its UTXO key.

### HTTP Method

`POST`

### RPC Method

`getOutput`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| [0] | string | Yes | Hex-encoded UTXO key to query output for |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| output_key | string | Unique identifier for the output |
| value | string | Output value in base currency units |
| block_height | integer | Block height when output was created |
| transaction_hash | string | Transaction hash containing this output |

---

### Get Specific Memo Output

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "getMemoOutput",
    "params": ["hex_encoded_utxo_key"],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'getMemoOutput',
    params: ['hex_encoded_utxo_key'],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "output_key": "bcdef1234567890abcdef1234567890abcdef1234...",
    "memo_data": "encrypted_memo_content",
    "block_height": 12353,
    "transaction_hash": "cdef1234567890abcdef1234567890abcdef1234..."
  },
  "id": 1
}
```

Retrieves a specific memo output by its UTXO key.

### HTTP Method

`POST`

### RPC Method

`getMemoOutput`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| [0] | string | Yes | Hex-encoded UTXO key to query memo output for |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| output_key | string | Unique identifier for the memo output |
| memo_data | string | Encrypted memo content |
| block_height | integer | Block height when memo output was created |
| transaction_hash | string | Transaction hash containing this memo output |

---

### Get Specific State Output

```shell
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "getStateOutput",
    "params": ["hex_encoded_utxo_key"],
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'getStateOutput',
    params: ['hex_encoded_utxo_key'],
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "output_key": "def1234567890abcdef1234567890abcdef123456...",
    "state_data": "encrypted_state_content",
    "block_height": 12354,
    "transaction_hash": "ef1234567890abcdef1234567890abcdef123456..."
  },
  "id": 1
}
```

Retrieves a specific state output by its UTXO key.

### HTTP Method

`POST`

### RPC Method

`getStateOutput`

### Message Parameters

| Params | Data_Type | Required | Values |
| ------ | --------- | -------- | ------ |
| [0] | string | Yes | Hex-encoded UTXO key to query state output for |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| output_key | string | Unique identifier for the state output |
| state_data | string | Encrypted state content |
| block_height | integer | Block height when state output was created |
| transaction_hash | string | Transaction hash containing this state output |

---

## Database Queries

### Query UTXOs from Database

> **Maximum limit:** 10,000 records per request. Requests exceeding this limit will be capped.

This method uses **named parameters** (object) instead of positional parameters (array).

```shell
# Query coin UTXOs
curl -X POST https://nykschain.twilight.rest/zkos/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "getUtxosFromDB",
    "params": {
      "start_block": 0,
      "end_block": 1000,
      "limit": 100,
      "pagination": 0,
      "io_type": "Coin"
    },
    "id": 1
  }'
```

```javascript
const response = await fetch('https://nykschain.twilight.rest/zkos/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    jsonrpc: '2.0',
    method: 'getUtxosFromDB',
    params: {
      start_block: 0,
      end_block: 1000,
      limit: 100,
      pagination: 0,
      io_type: 'Coin'
    },
    id: 1
  })
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "jsonrpc": "2.0",
  "result": [
    {
      "utxo_key": "1234567890abcdef1234567890abcdef12345678...",
      "block_height": 12355,
      "io_type": "Coin",
      "data": "encrypted_utxo_data"
    }
  ],
  "id": 1
}
```

Queries UTXOs from the PostgreSQL database with filtering by block range, type, and pagination.

### HTTP Method

`POST`

### RPC Method

`getUtxosFromDB`

### Message Parameters

| Field | Data_Type | Required | Values |
| ----- | --------- | -------- | ------ |
| start_block | integer | Yes | Starting block height |
| end_block | integer | Yes | Ending block height |
| limit | integer | Yes | Maximum number of results (max: 10,000) |
| pagination | integer | Yes | Pagination offset for result sets |
| io_type | string | Yes | Type of UTXO: `"Coin"`, `"Memo"`, or `"State"` |

### Response Fields

| Field | Data_Type | Description |
| ----- | --------- | ----------- |
| utxo_key | string | Unique identifier for the UTXO |
| block_height | integer | Block height when UTXO was created |
| io_type | string | Type of UTXO (Coin, Memo, or State) |
| data | string | Encrypted UTXO content based on type |

---

## Notes

1. All hex strings should be valid hexadecimal without the `0x` prefix
2. Some endpoints return empty results with error messages if no data is found
3. Transaction verification is performed before committing transactions
