## Cosmos Auth Module
 
## Accounts

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/auth/v1beta1/accounts \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/auth/v1beta1/accounts', {
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
  "accounts": [
    {
      "@type": "@type..."
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```


`GET /cosmos/auth/v1beta1/accounts`

*Accounts returns all the existing accounts*

Since: cosmos-sdk 0.43

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|
|pagination.reverse|query|boolean|false|reverse is set to true if results are to be returned in the descending order.|

#### Detailed descriptions

**pagination.key**: key is a value returned in PageResponse.next_key to begin
querying the next page most efficiently. Only one of offset or key
should be set.

**pagination.offset**: offset is a numeric offset that can be used when key is unavailable.
It is less efficient than using key. Only one of offset or key should
be set.

**pagination.limit**: limit is the total number of results to be returned in the result page.
If left empty it will default to a value to be set by each app.

**pagination.count_total**: count_total is set to true  to indicate that the result set should include
a count of the total number of items available for pagination in UIs.
count_total is only respected when offset is used. It is ignored when key
is set.

**pagination.reverse**: reverse is set to true if results are to be returned in the descending order.

Since: cosmos-sdk 0.43

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryAccountsResponse is the response type for the Query/Accounts RPC method.

Since: cosmos-sdk 0.43*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» accounts|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» pagination|object|false|none|pagination defines the pagination in the response.|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Account

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/auth/v1beta1/accounts/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/auth/v1beta1/accounts/string', {

> The result from the above endpoint looks like this:

```json
{
  "account": {
    "@type": "@type..."
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

`GET /cosmos/auth/v1beta1/accounts/{address}`

*Account returns account details based on address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|string|true|address defines the address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryAccountResponse is the response type for the Query/Account RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» account|object|false|none|account defines the account of the corresponding address.|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Params

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "params": {
    "max_memo_characters": "1000000",
    "tx_sig_limit": "1000000",
    "tx_size_cost_per_byte": "1000000",
    "sig_verify_cost_ed25519": "1000000",
    "sig_verify_cost_secp256k1": "1000000"
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/auth/v1beta1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/auth/v1beta1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/auth/v1beta1/params`

*Params queries all parameters.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryParamsResponse is the response type for the Query/Params RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» params|object|false|none|params defines the parameters of the module.|
|»» max_memo_characters|string(uint64)|false|none|none|
|»» tx_sig_limit|string(uint64)|false|none|none|
|»» tx_size_cost_per_byte|string(uint64)|false|none|none|
|»» sig_verify_cost_ed25519|string(uint64)|false|none|none|
|»» sig_verify_cost_secp256k1|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication
