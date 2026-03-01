# Forkscanner Module

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
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## DelegateKeysByBtcOracleAddress

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/forks/delegate_keys_by_btc_oracle_address/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/forks/delegate_keys_by_btc_oracle_address/string', {

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

  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
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
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication
