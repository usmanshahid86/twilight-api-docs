## Miscellaneous

## CosmosEvidenceV1Beta1AllEvidence

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/evidence/v1beta1/evidence \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/evidence/v1beta1/evidence', {
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
  "evidence": [
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


`GET /cosmos/evidence/v1beta1/evidence`

*AllEvidence queries all evidence.*

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

*QueryAllEvidenceResponse is the response type for the Query/AllEvidence RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» evidence|[object]|false|none|evidence returns all evidences.|
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

## CosmosEvidenceV1Beta1Evidence

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/evidence/v1beta1/evidence/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/evidence/v1beta1/evidence/string', {

> The result from the above endpoint looks like this:

```json
{
  "evidence": {
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

`GET /cosmos/evidence/v1beta1/evidence/{evidence_hash}`

*Evidence queries evidence based on evidence hash.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|evidence_hash|path|string(byte)|true|evidence_hash defines the hash of the requested evidence.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryEvidenceResponse is the response type for the Query/Evidence RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» evidence|object|false|none|evidence returns the requested evidence.|
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

## CosmosFeegrantV1Beta1Allowance

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "allowance": {
    "granter": "granter...",
    "grantee": "grantee...",
    "allowance": {
      "@type": "@type..."
    }
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/feegrant/v1beta1/allowance/string/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/feegrant/v1beta1/allowance/string/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/feegrant/v1beta1/allowance/{granter}/{grantee}`

*Allowance returns fee granted to the grantee by the granter.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|granter|path|string|true|granter is the address of the user granting an allowance of their funds.|
|grantee|path|string|true|grantee is the address of the user being granted an allowance of another user's funds.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryAllowanceResponse is the response type for the Query/Allowance RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» allowance|object|false|none|allowance is a allowance granted for grantee by granter.|
|»» granter|string|false|none|granter is the address of the user granting an allowance of their funds.|
|»» grantee|string|false|none|grantee is the address of the user being granted an allowance of another user's funds.|
|»» allowance|object|false|none|allowance can be any of basic and filtered fee allowance.|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|


> The result from the above endpoint looks like this:

```json
{
  "allowances": [
    {
      "granter": "granter...",
      "grantee": "grantee...",
      "allowance": {
        "@type": "@type..."
      }
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

> This operation does not require authentication

## CosmosFeegrantV1Beta1Allowances

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/feegrant/v1beta1/allowances/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/feegrant/v1beta1/allowances/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/feegrant/v1beta1/allowances/{grantee}`

*Allowances returns all the grants for address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|grantee|path|string|true|none|
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

*QueryAllowancesResponse is the response type for the Query/Allowances RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» allowances|[object]|false|none|allowances are allowance's granted for grantee by granter.|
|»» Grant is stored in the KVStore to record a grant with full context|object|false|none|none|
|»»» granter|string|false|none|granter is the address of the user granting an allowance of their funds.|
|»»» grantee|string|false|none|grantee is the address of the user being granted an allowance of another user's funds.|
|»»» allowance|object|false|none|allowance can be any of basic and filtered fee allowance.|
|»»»» **additionalProperties**|any|false|none|none|
|»»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» pagination|object|false|none|pagination defines an pagination for the response.|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "annual_provisions": "annual_provisions..."
}
```

|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## CosmosMintV1Beta1AnnualProvisions

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/mint/v1beta1/annual_provisions \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/mint/v1beta1/annual_provisions', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/mint/v1beta1/annual_provisions`

*AnnualProvisions current minting annual provisions value.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryAnnualProvisionsResponse is the response type for the
Query/AnnualProvisions RPC method.*


> The result from the above endpoint looks like this:

```json
{
  "inflation": "inflation..."
}
```

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» annual_provisions|string(byte)|false|none|annual_provisions is the current minting annual provisions value.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## CosmosMintV1Beta1Inflation

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/mint/v1beta1/inflation \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/mint/v1beta1/inflation', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/mint/v1beta1/inflation`

*Inflation returns the current minting inflation value.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|


> The result from the above endpoint looks like this:

```json
{
  "params": {
    "mint_denom": "mint_denom...",
    "inflation_rate_change": "inflation_rate_change...",
    "inflation_max": "inflation_max...",
    "inflation_min": "inflation_min...",
    "goal_bonded": "goal_bonded...",
    "blocks_per_year": "1000000"
  }
}
```

### Response Schema

Status Code **200**

*QueryInflationResponse is the response type for the Query/Inflation RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» inflation|string(byte)|false|none|inflation is the current minting inflation value.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## CosmosMintV1Beta1Params

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/mint/v1beta1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/mint/v1beta1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/mint/v1beta1/params`

*Params returns the total set of minting parameters.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|

> The result from the above endpoint looks like this:

```json
{
  "param": {
    "subspace": "subspace...",
    "key": "key...",
    "value": "1000"
  }
}
```

|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryParamsResponse is the response type for the Query/Params RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» params|object|false|none|params defines the parameters of the module.|
|»» mint_denom|string|false|none|none|
|»» inflation_rate_change|string|false|none|none|
|»» inflation_max|string|false|none|none|
|»» inflation_min|string|false|none|none|
|»» goal_bonded|string|false|none|none|
|»» blocks_per_year|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## CosmosParamsV1Beta1Params

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/params/v1beta1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/params/v1beta1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/params/v1beta1/params`

*Params queries a specific parameter of a module, given its subspace and
key.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|subspace|query|string|false|subspace defines the module to query the parameter for.|
|key|query|string|false|key defines the key of the parameter in the subspace.|

> The result from the above endpoint looks like this:

```json
{
  "height": "height..."
}
```


> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryParamsResponse is response type for the Query/Params RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» param|object|false|none|param defines the queried parameter.|
|»» subspace|string|false|none|none|
|»» key|string|false|none|none|
|»» value|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## CosmosUpgradeV1Beta1AppliedPlan

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/upgrade/v1beta1/applied_plan/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/upgrade/v1beta1/applied_plan/string', {
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
  "plan": {
    "name": "name...",
    "time": "time...",
    "height": "height...",
    "info": "info...",
    "upgraded_client_state": {
      "@type": "@type..."
    }
  }
}
```

`GET /cosmos/upgrade/v1beta1/applied_plan/{name}`

*AppliedPlan queries a previously applied upgrade plan by its name.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|name is the name of the applied plan to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryAppliedPlanResponse is the response type for the Query/AppliedPlan RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» height|string(int64)|false|none|height is the block height at which the plan was applied.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## CosmosUpgradeV1Beta1CurrentPlan

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/upgrade/v1beta1/current_plan \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/upgrade/v1beta1/current_plan', {
  headers: {
    'Accept': '*/*'

> The result from the above endpoint looks like this:

```json
{
  "module_versions": [
    {
      "name": "name...",
      "version": "1000000"
    }
  ]
}
```

  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/upgrade/v1beta1/current_plan`

*CurrentPlan queries the current upgrade plan.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryCurrentPlanResponse is the response type for the Query/CurrentPlan RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» plan|object|false|none|plan is the current upgrade plan.|
|»» name|string|false|none|Sets the name for the upgrade. This name will be used by the upgradedversion of the software to apply any special "on-upgrade" commands duringthe first BeginBlock method after the upgrade is applied. It is also usedto detect whether a software version can handle a given upgrade. If noupgrade handler with this name has been set in the software, it will beassumed that the software is out-of-date when the upgrade Time or Height isreached and the software will exit.|
|»» time|string(date-time)|false|none|Deprecated: Time based upgrades have been deprecated. Time based upgrade logichas been removed from the SDK.If this field is not empty, an error will be thrown.|
|»» height|string(int64)|false|none|The height at which the upgrade must be performed.Only used if Time is not set.|
|»» info|string|false|none|none|
|»» upgraded_client_state|object|false|none|Deprecated: UpgradedClientState field has been deprecated. IBC upgrade logic has beenmoved to the IBC module in the sub module 02-client.If this field is not empty, an error will be thrown.|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## CosmosUpgradeV1Beta1ModuleVersions

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/upgrade/v1beta1/module_versions \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/upgrade/v1beta1/module_versions', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);

> The result from the above endpoint looks like this:

```json
{
  "upgraded_consensus_state": "upgraded_consensus_state..."
}
```

```

`GET /cosmos/upgrade/v1beta1/module_versions`

*ModuleVersions queries the list of module versions from state.*

Since: cosmos-sdk 0.43

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|module_name|query|string|false|module_name is a field to query a specific module|

#### Detailed descriptions

**module_name**: module_name is a field to query a specific module
consensus version from state. Leaving this empty will
fetch the full list of module versions from state

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryModuleVersionsResponse is the response type for the Query/ModuleVersions
RPC method.

Since: cosmos-sdk 0.43*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» module_versions|[object]|false|none|module_versions is a list of module names with their consensus versions.|
|»» name|string|false|none|none|
|»» version|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## CosmosUpgradeV1Beta1UpgradedConsensusState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/upgrade/v1beta1/upgraded_consensus_state/string \
  --header 'Accept: */*'
```

> The result from the above endpoint looks like this:

```json
{
  "attestations": [
    {
      "observed": true,
      "votes": [
        "item..."
      ],
      "height": "1000000",
      "proposal": {
        "@type": "@type..."
      }
    }
  ]
}
```


```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/upgrade/v1beta1/upgraded_consensus_state/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height}`

*UpgradedConsensusState queries the consensus state that will serve
as a trusted kernel for the next version of this chain. It will only be
stored at the last height of this chain.
UpgradedConsensusState RPC not supported with legacy querier
This rpc is deprecated now that IBC has its own replacement
(https://github.com/cosmos/ibc-go/blob/2c880a22e9f9cc75f62b527ca94aa75ce1106001/proto/ibc/core/client/v1/query.proto#L54)*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|last_height|path|string(int64)|true|last height of the current chain must be sent in request|

#### Detailed descriptions

**last_height**: last height of the current chain must be sent in request
as this is the height under which next consensus state is stored

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryUpgradedConsensusStateResponse is the response type for the Query/UpgradedConsensusState
RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» upgraded_consensus_state|string(byte)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## TwilightprojectNyksForksGetAttestations

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/nyks/attestations \
  --header 'Accept: */*'
```

> The result from the above endpoint looks like this:

```json
{
  "params": {}
}
```


```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/nyks/attestations', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/nyks/attestations`

*Queries a list of Attestations items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string(uint64)|false|limit defines how many attestations to limit in the response.|
|order_by|query|string|false|order_by provides ordering of atteststions by nonce in the response. Either|
|proposal_type|query|string|false|proposal_type allows filtering attestations by proposal type|
|height|query|string(uint64)|false|height allows filtering attestations by block height|

#### Detailed descriptions

**order_by**: order_by provides ordering of atteststions by nonce in the response. Either
'asc' or 'desc' can be provided. If no value is provided, it defaults to
'asc'.

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
|» attestations|[object]|false|none|none|
|»» Attestation is an aggregate of `proposals` that eventually becomes `observed` by
all orchestrators
OBSERVED:
Observed indicates that >67% of validators have attested to the event,
and that the event should be executed by the state machine|object|false|none|The actual content of the proposals is passed in with the transaction making the proposaland then passed through the call stack alongside the attestation while it is processedthe key in which the attestation is stored is keyed on the exact details of the proposalbut there is no reason to store those exact details becuause the next message senderwill kindly provide you with them.|
|»»» observed|boolean|false|none|none|
|»»» votes|[string]|false|none|none|
|»»» height|string(uint64)|false|none|none|
|»»» proposal|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»»» **additionalProperties**|any|false|none|none|
|»»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## TwilightprojectNyksForksParams

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilightproject/nyks/nyks/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilightproject/nyks/nyks/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilightproject/nyks/nyks/params`

*Parameters queries the parameters of the module.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryParamsResponse is response type for the Query/Params RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» params|object|false|none|params holds all the parameters of this module.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication
