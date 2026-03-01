# Nyks Bank Module

## AllBalances

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/balances/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/balances/string', {
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
  "balances": [
    {
      "denom": "denom...",
      "amount": "1000"
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```


`GET /cosmos/bank/v1beta1/balances/{address}`

*AllBalances queries the balance of all coins for a single account.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|string|true|address is the address to query balances for.|
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

*QueryAllBalancesResponse is the response type for the Query/AllBalances RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» balances|[object]|false|none|balances is the balances of all the coins.|
|»» denom|string|false|none|none|
|»» amount|string|false|none|none|
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
|»» @type|string|false|none|none|

> This operation does not require authentication

## Balance

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/balances/string/by_denom \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/balances/string/by_denom', {

> The result from the above endpoint looks like this:

```json
{
  "balance": {
    "denom": "denom...",
    "amount": "1000"
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

`GET /cosmos/bank/v1beta1/balances/{address}/by_denom`

*Balance queries the balance of a single coin for a single account.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|string|true|address is the address to query balances for.|
|denom|query|string|false|denom is the coin denom to query balances for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryBalanceResponse is the response type for the Query/Balance RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» balance|object|false|none|balance is the balance of the coin.|
|»» denom|string|false|none|none|
|»» amount|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## DenomsMetadata

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "metadatas": [
    {
      "description": "description...",
      "denom_units": [
        {
          "denom": "denom...",
          "exponent": 0,
          "aliases": [
            "item..."
          ]
        }
      ],
      "base": "base..."
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/denoms_metadata \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/denoms_metadata', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/bank/v1beta1/denoms_metadata`

*DenomsMetadata queries the client metadata for all registered coin denominations.*

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

*QueryDenomsMetadataResponse is the response type for the Query/DenomsMetadata RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» metadatas|[object]|false|none|metadata provides the client information for all the registered tokens.|
|»» description|string|false|none|none|
|»» denom_units|[object]|false|none|none|
|»»» denom|string|false|none|denom represents the string name of the given denom unit (e.g uatom).|
|»»» exponent|integer(int64)|false|none|exponent represents power of 10 exponent that one mustraise the base_denom to in order to equal the given DenomUnit's denom1 denom = 1^exponent base_denom(e.g. with a base_denom of uatom, one can create a DenomUnit of 'atom' withexponent = 6, thus: 1 atom = 10^6 uatom).|
|»»» aliases|[string]|false|none|none|
|»» base|string|false|none|base represents the base denom (should be the DenomUnit with exponent = 0).|
|»» display|string|false|none|display indicates the suggested denom that should bedisplayed in clients.|
|»» name|string|false|none|Since: cosmos-sdk 0.43|
|»» symbol|string|false|none|symbol is the token symbol usually shown on exchanges (eg: ATOM). This canbe the same as the display.Since: cosmos-sdk 0.43|
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
|»» @type|string|false|none|none|


> The result from the above endpoint looks like this:

```json
{
  "metadata": {
    "description": "description...",
    "denom_units": [
      {
        "denom": "denom...",
        "exponent": 0,
        "aliases": [
          "item..."
        ]
      }
    ],
    "base": "base...",
    "display": "display...",
    "name": "name...",
    "symbol": "symbol..."
  }
}
```

> This operation does not require authentication

## DenomMetadata

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/denoms_metadata/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/denoms_metadata/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/bank/v1beta1/denoms_metadata/{denom}`

*DenomsMetadata queries the client metadata of a given coin denomination.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|denom|path|string|true|denom is the coin denom to query the metadata for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDenomMetadataResponse is the response type for the Query/DenomMetadata RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» metadata|object|false|none|metadata describes and provides all the client information for the requested token.|
|»» description|string|false|none|none|
|»» denom_units|[object]|false|none|none|
|»»» denom|string|false|none|denom represents the string name of the given denom unit (e.g uatom).|
|»»» exponent|integer(int64)|false|none|exponent represents power of 10 exponent that one mustraise the base_denom to in order to equal the given DenomUnit's denom1 denom = 1^exponent base_denom(e.g. with a base_denom of uatom, one can create a DenomUnit of 'atom' withexponent = 6, thus: 1 atom = 10^6 uatom).|
|»»» aliases|[string]|false|none|none|
|»» base|string|false|none|base represents the base denom (should be the DenomUnit with exponent = 0).|
|»» display|string|false|none|display indicates the suggested denom that should bedisplayed in clients.|
|»» name|string|false|none|Since: cosmos-sdk 0.43|
|»» symbol|string|false|none|symbol is the token symbol usually shown on exchanges (eg: ATOM). This canbe the same as the display.Since: cosmos-sdk 0.43|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "params": {
    "send_enabled": [
      {
        "denom": "denom...",
        "enabled": true
      }
    ],
    "default_send_enabled": true
  }
}
```

|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## Params

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/bank/v1beta1/params`

*Params queries the parameters of x/bank module.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryParamsResponse defines the response type for querying x/bank parameters.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» params|object|false|none|Params defines the parameters for the bank module.|
|»» send_enabled|[object]|false|none|none|

> The result from the above endpoint looks like this:

```json
{
  "balances": [
    {
      "denom": "denom...",
      "amount": "1000"
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

|»»» denom|string|false|none|none|
|»»» enabled|boolean|false|none|none|
|»» default_send_enabled|boolean|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## SpendableBalances

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/spendable_balances/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/spendable_balances/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/bank/v1beta1/spendable_balances/{address}`

*SpendableBalances queries the spenable balance of all coins for a single
account.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|string|true|address is the address to query spendable balances for.|
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

*QuerySpendableBalancesResponse defines the gRPC response structure for querying

> The result from the above endpoint looks like this:

```json
{
  "supply": [
    {
      "denom": "denom...",
      "amount": "1000"
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

an account's spendable balances.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» balances|[object]|false|none|balances is the spendable balances of all the coins.|
|»» denom|string|false|none|none|
|»» amount|string|false|none|none|
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
|»» @type|string|false|none|none|

> This operation does not require authentication

## TotalSupply

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/supply \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/supply', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/bank/v1beta1/supply`

*TotalSupply queries the total supply of all coins.*

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

> The result from the above endpoint looks like this:

```json
{
  "amount": {
    "denom": "denom...",
    "amount": "1000"
  }
}
```

|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryTotalSupplyResponse is the response type for the Query/TotalSupply RPC
method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» supply|[object]|false|none|none|
|»» denom|string|false|none|none|
|»» amount|string|false|none|none|
|» pagination|object|false|none|pagination defines the pagination in the response.Since: cosmos-sdk 0.43|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## SupplyOf

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/bank/v1beta1/supply/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/bank/v1beta1/supply/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/bank/v1beta1/supply/{denom}`

*SupplyOf queries the supply of a single coin.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|denom|path|string|true|denom is the coin denom to query balances for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QuerySupplyOfResponse is the response type for the Query/SupplyOf RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» amount|object|false|none|amount is the supply of the coin.|
|»» denom|string|false|none|none|
|»» amount|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication
