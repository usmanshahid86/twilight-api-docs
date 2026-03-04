# Forkscanner Module

The Forks module (Forkscanner) manages validator delegate key mappings. Validators register their BTC oracle address, public key, and zkOS oracle address through this module. These delegate keys are used by the bridge module for BTC chain tip attestation and the zkOS module for oracle operations.

**Base URL:** `https://lcd.twilight.org`

---

## DelegateKeysAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/forks/delegate_keys_all \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/forks/delegate_keys_all', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "addresses": [
    {
      "validatorAddress": "0x1234567890abcdef...",
      "btcOracleAddress": "0x1234567890abcdef...",
      "btcPublicKey": "btcPublicKey...",
      "zkOracleAddress": "0x1234567890abcdef..."
    }
  ]
}
```

`GET /twilight-project/nyks/forks/delegate_keys_all`

*Queries a list of DelegateKeysAll items.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» addresses|[object]|false|none|none|
|»» validatorAddress|string|false|none|none|
|»» btcOracleAddress|string|false|none|none|
|»» btcPublicKey|string|false|none|none|
|»» zkOracleAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|

> This operation does not require authentication

## DelegateKeysByBtcOracleAddress

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/forks/delegate_keys_by_btc_oracle_address/{btcOracleAddress} \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/forks/delegate_keys_by_btc_oracle_address/{btcOracleAddress}', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

> The result from the above endpoint looks like this:

```json
{
  "addresses": {
    "validatorAddress": "0x1234567890abcdef...",
    "btcOracleAddress": "0x1234567890abcdef...",
    "btcPublicKey": "btcPublicKey...",
    "zkOracleAddress": "0x1234567890abcdef..."
  }
}
```

`GET /twilight-project/nyks/forks/delegate_keys_by_btc_oracle_address/{btcOracleAddress}`

*Queries a list of DelegateKeysByBtcOracleAddress items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|btcOracleAddress|path|string|true|none|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» addresses|object|false|none|none|
|»» validatorAddress|string|false|none|none|
|»» btcOracleAddress|string|false|none|none|
|»» btcPublicKey|string|false|none|none|
|»» zkOracleAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|

> This operation does not require authentication
