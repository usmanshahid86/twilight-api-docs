# Twilight Chain API

## ZKOS Module

The ZKOS module provides REST API endpoints for querying ZKOS-related data on the Twilight chain.

**Base URL:** `https://lcd.twilight.org`

> 🔐 No authentication required.

---

## Endpoints

### Mint or Burn Trading BTC

```shell
curl -X GET https://lcd.twilight.org/twilight-project/nyks/zkos/mint_or_burn_trading_btc/{twilightAddress} \
  -H 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/zkos/mint_or_burn_trading_btc/{twilightAddress}');
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/zkos/mint_or_burn_trading_btc/{twilightAddress}`

*Queries a list of MintOrBurnTradingBtc items.*

#### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|twilightAddress|path|string|true|The Twilight address to query|

#### Responses

|Status|Meaning|Description|
|---|---|---|
|200|OK|A successful response|
|default|Default|An unexpected error response|

#### Response Schema (200)

|Name|Type|Required|Description|
|---|---|---|---|
|mintOrBurn|boolean|false|Whether this is a mint or burn operation|
|btcValue|string(uint64)|false|The BTC value|
|qqAccount|string|false|The QQ account address|
|encryptScalar|string|false|The encrypted scalar|
|twilightAddress|string|false|The Twilight address|

> This operation does not require authentication

---

### Get ZKOS Parameters

```shell
curl -X GET https://lcd.twilight.org/twilight-project/nyks/zkos/params \
  -H 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/zkos/params');
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/zkos/params`

*Parameters queries the parameters of the module.*

#### Responses

|Status|Meaning|Description|
|---|---|---|
|200|OK|A successful response|
|default|Default|An unexpected error response|

#### Response Schema (200)

*QueryParamsResponse is response type for the Query/Params RPC method.*

|Name|Type|Required|Description|
|---|---|---|---|
|params|object|false|params holds all the parameters of this module|

> This operation does not require authentication

---

### Get Transfer Transaction

```shell
curl -X GET https://lcd.twilight.org/twilight-project/nyks/zkos/transfer_tx/{txId} \
  -H 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/zkos/transfer_tx/{txId}');
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/zkos/transfer_tx/{txId}`

*Queries a list of TransferTx items.*

#### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|The transaction ID to query|

#### Responses

|Status|Meaning|Description|
|---|---|---|
|200|OK|A successful response|
|default|Default|An unexpected error response|

#### Response Schema (200)

|Name|Type|Required|Description|
|---|---|---|---|
|txId|string|false|The transaction ID|
|txByteCode|string|false|The transaction bytecode|
|txFee|string(uint64)|false|The transaction fee|
|zkOracleAddress|string|false|The ZK Oracle address|

> This operation does not require authentication
