x## Cosmos Staking Module

## DelegatorDelegations

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/delegations/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/delegations/string', {
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
  "delegation_responses": [
    {
      "delegation": {
        "delegator_address": "0x1234567890abcdef...",
        "validator_address": "0x1234567890abcdef...",
        "shares": "shares..."
      },
      "balance": {
        "denom": "denom...",
        "amount": "1000"
      }
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```


`GET /cosmos/staking/v1beta1/delegations/{delegator_addr}`

*DelegatorDelegations queries all delegations of a given delegator address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_addr|path|string|true|delegator_addr defines the delegator address to query for.|
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

*QueryDelegatorDelegationsResponse is response type for the
Query/DelegatorDelegations RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» delegation_responses|[object]|false|none|delegation_responses defines all the delegations' info of a delegator.|
|»» delegation|object|false|none|Delegation represents the bond with tokens held by an account. It isowned by one delegator, and is associated with the voting power of onevalidator.|
|»»» delegator_address|string|false|none|delegator_address is the bech32-encoded address of the delegator.|
|»»» validator_address|string|false|none|validator_address is the bech32-encoded address of the validator.|
|»»» shares|string|false|none|shares define the delegation shares received.|
|»» balance|object|false|none|Coin defines a token with a denomination and an amount.NOTE: The amount field is an Int which implements the custom methodsignatures required by gogoproto.|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|
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

## Redelegations

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/redelegations \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/redelegations', {

> The result from the above endpoint looks like this:

```json
{
  "redelegation_responses": [
    {
      "redelegation": {
        "delegator_address": "0x1234567890abcdef...",
        "validator_src_address": "0x1234567890abcdef...",
        "validator_dst_address": "0x1234567890abcdef..."
      },
      "entries": [
        {
          "redelegation_entry": {
            "creation_height": "creation_height...",
            "completion_time": "completion_time...",
            "initial_balance": "initial_balance..."
          },
          "balance": "balance..."
        }
      ]
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
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

`GET /cosmos/staking/v1beta1/delegators/{delegator_addr}/redelegations`

*Redelegations queries redelegations of given address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_addr|path|string|true|delegator_addr defines the delegator address to query for.|
|src_validator_addr|query|string|false|src_validator_addr defines the validator address to redelegate from.|
|dst_validator_addr|query|string|false|dst_validator_addr defines the validator address to redelegate to.|
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

*QueryRedelegationsResponse is response type for the Query/Redelegations RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» redelegation_responses|[object]|false|none|none|
|»» redelegation|object|false|none|Redelegation contains the list of a particular delegator's redelegating bondsfrom a particular source validator to a particular destination validator.|
|»»» delegator_address|string|false|none|delegator_address is the bech32-encoded address of the delegator.|
|»»» validator_src_address|string|false|none|validator_src_address is the validator redelegation source operator address.|
|»»» validator_dst_address|string|false|none|validator_dst_address is the validator redelegation destination operator address.|
|»»» entries|[object]|false|none|entries are the redelegation entries.redelegation entries|
|»»»» creation_height|string(int64)|false|none|creation_height  defines the height which the redelegation took place.|
|»»»» completion_time|string(date-time)|false|none|completion_time defines the unix time for redelegation completion.|
|»»»» initial_balance|string|false|none|initial_balance defines the initial balance when redelegation started.|
|»»»» shares_dst|string|false|none|shares_dst is the amount of destination-validator shares created by redelegation.|
|»» entries|[object]|false|none|none|
|»»» redelegation_entry|object|false|none|RedelegationEntry defines a redelegation object with relevant metadata.|
|»»»» creation_height|string(int64)|false|none|creation_height  defines the height which the redelegation took place.|
|»»»» completion_time|string(date-time)|false|none|completion_time defines the unix time for redelegation completion.|
|»»»» initial_balance|string|false|none|initial_balance defines the initial balance when redelegation started.|
|»»»» shares_dst|string|false|none|shares_dst is the amount of destination-validator shares created by redelegation.|
|»»» balance|string|false|none|none|
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

## DelegatorUnbondingDelegations

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "unbonding_responses": [
    {
      "delegator_address": "0x1234567890abcdef...",
      "validator_address": "0x1234567890abcdef...",
      "entries": [
        {
          "creation_height": "creation_height...",
          "completion_time": "completion_time...",
          "initial_balance": "initial_balance..."
        }
      ]
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/unbonding_delegations \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/unbonding_delegations', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/delegators/{delegator_addr}/unbonding_delegations`

*DelegatorUnbondingDelegations queries all unbonding delegations of a given
delegator address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_addr|path|string|true|delegator_addr defines the delegator address to query for.|
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

*QueryUnbondingDelegatorDelegationsResponse is response type for the
Query/UnbondingDelegatorDelegations RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» unbonding_responses|[object]|false|none|none|
|»» delegator_address|string|false|none|delegator_address is the bech32-encoded address of the delegator.|
|»» validator_address|string|false|none|validator_address is the bech32-encoded address of the validator.|
|»» entries|[object]|false|none|entries are the unbonding delegation entries.unbonding delegation entries|
|»»» creation_height|string(int64)|false|none|creation_height is the height which the unbonding took place.|
|»»» completion_time|string(date-time)|false|none|completion_time is the unix time for unbonding completion.|
|»»» initial_balance|string|false|none|initial_balance defines the tokens initially scheduled to receive at completion.|
|»»» balance|string|false|none|balance defines the tokens to receive at completion.|
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


> The result from the above endpoint looks like this:

```json
{
  "validators": [
    {
      "operator_address": "0x1234567890abcdef...",
      "consensus_pubkey": {
        "@type": "@type..."
      },
      "jailed": true
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

> This operation does not require authentication

## DelegatorValidators

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/validators \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/validators', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/delegators/{delegator_addr}/validators`

*DelegatorValidators queries all validators info for given delegator
address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_addr|path|string|true|delegator_addr defines the delegator address to query for.|
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

*QueryDelegatorValidatorsResponse is response type for the
Query/DelegatorValidators RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» validators|[object]|false|none|validators defines the the validators' info of a delegator.|
|»» operator_address|string|false|none|operator_address defines the address of the validator's operator; bech encoded in JSON.|
|»» consensus_pubkey|object|false|none|consensus_pubkey is the consensus public key of the validator, as a Protobuf Any.|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» jailed|boolean|false|none|jailed defined whether the validator has been jailed from bonded status or not.|
|»» status|string|false|none|status is the validator status (bonded/unbonding/unbonded).|
|»» tokens|string|false|none|tokens define the delegated tokens (incl. self-delegation).|
|»» delegator_shares|string|false|none|delegator_shares defines total shares issued to a validator's delegators.|
|»» description|object|false|none|description defines the description terms for the validator.|
|»»» moniker|string|false|none|moniker defines a human-readable name for the validator.|
|»»» identity|string|false|none|identity defines an optional identity signature (ex. UPort or Keybase).|
|»»» website|string|false|none|website defines an optional website link.|
|»»» security_contact|string|false|none|security_contact defines an optional email for security contact.|
|»»» details|string|false|none|details define other optional details.|
|»» unbonding_height|string(int64)|false|none|unbonding_height defines, if unbonding, the height at which this validator has begun unbonding.|
|»» unbonding_time|string(date-time)|false|none|unbonding_time defines, if unbonding, the min time for the validator to complete unbonding.|
|»» commission|object|false|none|commission defines the commission parameters.|
|»»» commission_rates|object|false|none|commission_rates defines the initial commission rates to be used for creating a validator.|
|»»»» rate|string|false|none|rate is the commission rate charged to delegators, as a fraction.|
|»»»» max_rate|string|false|none|max_rate defines the maximum commission rate which validator can ever charge, as a fraction.|
|»»»» max_change_rate|string|false|none|max_change_rate defines the maximum daily increase of the validator commission, as a fraction.|
|»»» update_time|string(date-time)|false|none|update_time is the last time the commission rate was changed.|
|»» min_self_delegation|string|false|none|min_self_delegation is the validator's self declared minimum self delegation.|
|» pagination|object|false|none|pagination defines the pagination in the response.|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|BOND_STATUS_UNSPECIFIED|
|status|BOND_STATUS_UNBONDED|
|status|BOND_STATUS_UNBONDING|
|status|BOND_STATUS_BONDED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "validator": {
    "operator_address": "0x1234567890abcdef...",
    "consensus_pubkey": {
      "@type": "@type..."
    },
    "jailed": true,
    "status": "status...",
    "tokens": "tokens...",
    "delegator_shares": "delegator_shares...",
    "description": {
      "moniker": "moniker...",
      "identity": "0x1234567890abcdef...",
      "website": "website..."
    },
    "unbonding_height": "unbonding_height...",
    "unbonding_time": "unbonding_time...",
    "commission": {
      "commission_rates": {
        "rate": "rate...",
        "max_rate": "max_rate...",
        "max_change_rate": "max_change_rate..."
      },
      "update_time": "update_time..."
    },
    "min_self_delegation": "min_self_delegation..."
  }
}
```

|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## DelegatorValidator

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/validators/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/delegators/string/validators/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/delegators/{delegator_addr}/validators/{validator_addr}`

*DelegatorValidator queries validator info for given delegator validator
pair.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_addr|path|string|true|delegator_addr defines the delegator address to query for.|
|validator_addr|path|string|true|validator_addr defines the validator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDelegatorValidatorResponse response type for the
Query/DelegatorValidator RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» validator|object|false|none|validator defines the the validator info.|
|»» operator_address|string|false|none|operator_address defines the address of the validator's operator; bech encoded in JSON.|
|»» consensus_pubkey|object|false|none|consensus_pubkey is the consensus public key of the validator, as a Protobuf Any.|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» jailed|boolean|false|none|jailed defined whether the validator has been jailed from bonded status or not.|
|»» status|string|false|none|status is the validator status (bonded/unbonding/unbonded).|
|»» tokens|string|false|none|tokens define the delegated tokens (incl. self-delegation).|
|»» delegator_shares|string|false|none|delegator_shares defines total shares issued to a validator's delegators.|
|»» description|object|false|none|description defines the description terms for the validator.|
|»»» moniker|string|false|none|moniker defines a human-readable name for the validator.|
|»»» identity|string|false|none|identity defines an optional identity signature (ex. UPort or Keybase).|
|»»» website|string|false|none|website defines an optional website link.|
|»»» security_contact|string|false|none|security_contact defines an optional email for security contact.|
|»»» details|string|false|none|details define other optional details.|
|»» unbonding_height|string(int64)|false|none|unbonding_height defines, if unbonding, the height at which this validator has begun unbonding.|
|»» unbonding_time|string(date-time)|false|none|unbonding_time defines, if unbonding, the min time for the validator to complete unbonding.|
|»» commission|object|false|none|commission defines the commission parameters.|
|»»» commission_rates|object|false|none|commission_rates defines the initial commission rates to be used for creating a validator.|
|»»»» rate|string|false|none|rate is the commission rate charged to delegators, as a fraction.|
|»»»» max_rate|string|false|none|max_rate defines the maximum commission rate which validator can ever charge, as a fraction.|
|»»»» max_change_rate|string|false|none|max_change_rate defines the maximum daily increase of the validator commission, as a fraction.|
|»»» update_time|string(date-time)|false|none|update_time is the last time the commission rate was changed.|
|»» min_self_delegation|string|false|none|min_self_delegation is the validator's self declared minimum self delegation.|

#### Enumerated Values

|Property|Value|
|---|---|
|status|BOND_STATUS_UNSPECIFIED|

> The result from the above endpoint looks like this:

```json
{
  "hist": {
    "header": {
      "version": {
        "block": "1000000",
        "app": "1000000"
      },
      "chain_id": "0x1234567890abcdef...",
      "height": "height..."
    },
    "valset": [
      {
        "operator_address": "0x1234567890abcdef...",
        "consensus_pubkey": {
          "@type": "@type..."
        },
        "jailed": true
      }
    ]
  }
}
```

|status|BOND_STATUS_UNBONDED|
|status|BOND_STATUS_UNBONDING|
|status|BOND_STATUS_BONDED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## HistoricalInfo

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/historical_info/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/historical_info/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/historical_info/{height}`

*HistoricalInfo queries the historical info for given height.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|height|path|string(int64)|true|height defines at which height to query the historical info.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryHistoricalInfoResponse is response type for the Query/HistoricalInfo RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» hist|object|false|none|hist defines the historical info at the given height.|
|»» header|object|false|none|Header defines the structure of a Tendermint block header.|
|»»» version|object|false|none|Consensus captures the consensus rules for processing a block in the blockchain,including all blockchain data structures and the rules of the application'sstate transition machine.|
|»»»» block|string(uint64)|false|none|none|
|»»»» app|string(uint64)|false|none|none|
|»»» chain_id|string|false|none|none|
|»»» height|string(int64)|false|none|none|
|»»» time|string(date-time)|false|none|none|
|»»» last_block_id|object|false|none|none|
|»»»» hash|string(byte)|false|none|none|
|»»»» part_set_header|object|false|none|none|
|»»»»» total|integer(int64)|false|none|none|
|»»»»» hash|string(byte)|false|none|none|
|»»» last_commit_hash|string(byte)|false|none|commit from validators from the last block|
|»»» data_hash|string(byte)|false|none|none|
|»»» validators_hash|string(byte)|false|none|validators for the current block|
|»»» next_validators_hash|string(byte)|false|none|none|
|»»» consensus_hash|string(byte)|false|none|none|
|»»» app_hash|string(byte)|false|none|none|
|»»» last_results_hash|string(byte)|false|none|none|
|»»» evidence_hash|string(byte)|false|none|evidence included in the block|
|»»» proposer_address|string(byte)|false|none|none|
|»» valset|[object]|false|none|none|
|»»» operator_address|string|false|none|operator_address defines the address of the validator's operator; bech encoded in JSON.|
|»»» consensus_pubkey|object|false|none|consensus_pubkey is the consensus public key of the validator, as a Protobuf Any.|
|»»»» **additionalProperties**|any|false|none|none|
|»»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»»» jailed|boolean|false|none|jailed defined whether the validator has been jailed from bonded status or not.|
|»»» status|string|false|none|status is the validator status (bonded/unbonding/unbonded).|
|»»» tokens|string|false|none|tokens define the delegated tokens (incl. self-delegation).|
|»»» delegator_shares|string|false|none|delegator_shares defines total shares issued to a validator's delegators.|
|»»» description|object|false|none|description defines the description terms for the validator.|
|»»»» moniker|string|false|none|moniker defines a human-readable name for the validator.|
|»»»» identity|string|false|none|identity defines an optional identity signature (ex. UPort or Keybase).|
|»»»» website|string|false|none|website defines an optional website link.|
|»»»» security_contact|string|false|none|security_contact defines an optional email for security contact.|
|»»»» details|string|false|none|details define other optional details.|
|»»» unbonding_height|string(int64)|false|none|unbonding_height defines, if unbonding, the height at which this validator has begun unbonding.|
|»»» unbonding_time|string(date-time)|false|none|unbonding_time defines, if unbonding, the min time for the validator to complete unbonding.|
|»»» commission|object|false|none|commission defines the commission parameters.|
|»»»» commission_rates|object|false|none|commission_rates defines the initial commission rates to be used for creating a validator.|
|»»»»» rate|string|false|none|rate is the commission rate charged to delegators, as a fraction.|
|»»»»» max_rate|string|false|none|max_rate defines the maximum commission rate which validator can ever charge, as a fraction.|
|»»»»» max_change_rate|string|false|none|max_change_rate defines the maximum daily increase of the validator commission, as a fraction.|
|»»»» update_time|string(date-time)|false|none|update_time is the last time the commission rate was changed.|

> The result from the above endpoint looks like this:

```json
{
  "params": {
    "unbonding_time": "unbonding_time...",
    "max_validators": 0,
    "max_entries": 0,
    "historical_entries": 0,
    "bond_denom": "bond_denom..."
  }
}
```

|»»» min_self_delegation|string|false|none|min_self_delegation is the validator's self declared minimum self delegation.|

#### Enumerated Values

|Property|Value|
|---|---|
|status|BOND_STATUS_UNSPECIFIED|
|status|BOND_STATUS_UNBONDED|
|status|BOND_STATUS_UNBONDING|
|status|BOND_STATUS_BONDED|

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
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/params`

*Parameters queries the staking parameters.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|

> The result from the above endpoint looks like this:

```json
{
  "pool": {
    "not_bonded_tokens": "not_bonded_tokens...",
    "bonded_tokens": "bonded_tokens..."
  }
}
```

|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryParamsResponse is response type for the Query/Params RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» params|object|false|none|params holds all the parameters of this module.|
|»» unbonding_time|string|false|none|unbonding_time is the time duration of unbonding.|
|»» max_validators|integer(int64)|false|none|max_validators is the maximum number of validators.|
|»» max_entries|integer(int64)|false|none|max_entries is the max entries for either unbonding delegation or redelegation (per pair/trio).|
|»» historical_entries|integer(int64)|false|none|historical_entries is the number of historical entries to persist.|
|»» bond_denom|string|false|none|bond_denom defines the bondable coin denomination.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Pool

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/pool \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/pool', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/pool`


> The result from the above endpoint looks like this:

```json
{
  "validators": [
    {
      "operator_address": "0x1234567890abcdef...",
      "consensus_pubkey": {
        "@type": "@type..."
      },
      "jailed": true
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

*Pool queries the pool info.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryPoolResponse is response type for the Query/Pool RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» pool|object|false|none|pool defines the pool info.|
|»» not_bonded_tokens|string|false|none|none|
|»» bonded_tokens|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Validators

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/validators \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/validators', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/validators`

*Validators queries all validators that match the given status.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|status|query|string|false|status enables to query for validators matching a given status.|
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

*QueryValidatorsResponse is response type for the Query/Validators RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» validators|[object]|false|none|validators contains all the queried validators.|
|»» operator_address|string|false|none|operator_address defines the address of the validator's operator; bech encoded in JSON.|
|»» consensus_pubkey|object|false|none|consensus_pubkey is the consensus public key of the validator, as a Protobuf Any.|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> The result from the above endpoint looks like this:

```json
{
  "validator": {
    "operator_address": "0x1234567890abcdef...",
    "consensus_pubkey": {
      "@type": "@type..."
    },
    "jailed": true,
    "status": "status...",
    "tokens": "tokens...",
    "delegator_shares": "delegator_shares...",
    "description": {
      "moniker": "moniker...",
      "identity": "0x1234567890abcdef...",
      "website": "website..."
    },
    "unbonding_height": "unbonding_height...",
    "unbonding_time": "unbonding_time...",
    "commission": {
      "commission_rates": {
        "rate": "rate...",
        "max_rate": "max_rate...",
        "max_change_rate": "max_change_rate..."
      },
      "update_time": "update_time..."
    },
    "min_self_delegation": "min_self_delegation..."
  }
}
```

|»» jailed|boolean|false|none|jailed defined whether the validator has been jailed from bonded status or not.|
|»» status|string|false|none|status is the validator status (bonded/unbonding/unbonded).|
|»» tokens|string|false|none|tokens define the delegated tokens (incl. self-delegation).|
|»» delegator_shares|string|false|none|delegator_shares defines total shares issued to a validator's delegators.|
|»» description|object|false|none|description defines the description terms for the validator.|
|»»» moniker|string|false|none|moniker defines a human-readable name for the validator.|
|»»» identity|string|false|none|identity defines an optional identity signature (ex. UPort or Keybase).|
|»»» website|string|false|none|website defines an optional website link.|
|»»» security_contact|string|false|none|security_contact defines an optional email for security contact.|
|»»» details|string|false|none|details define other optional details.|
|»» unbonding_height|string(int64)|false|none|unbonding_height defines, if unbonding, the height at which this validator has begun unbonding.|
|»» unbonding_time|string(date-time)|false|none|unbonding_time defines, if unbonding, the min time for the validator to complete unbonding.|
|»» commission|object|false|none|commission defines the commission parameters.|
|»»» commission_rates|object|false|none|commission_rates defines the initial commission rates to be used for creating a validator.|
|»»»» rate|string|false|none|rate is the commission rate charged to delegators, as a fraction.|
|»»»» max_rate|string|false|none|max_rate defines the maximum commission rate which validator can ever charge, as a fraction.|
|»»»» max_change_rate|string|false|none|max_change_rate defines the maximum daily increase of the validator commission, as a fraction.|
|»»» update_time|string(date-time)|false|none|update_time is the last time the commission rate was changed.|
|»» min_self_delegation|string|false|none|min_self_delegation is the validator's self declared minimum self delegation.|
|» pagination|object|false|none|pagination defines the pagination in the response.|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|BOND_STATUS_UNSPECIFIED|
|status|BOND_STATUS_UNBONDED|
|status|BOND_STATUS_UNBONDING|
|status|BOND_STATUS_BONDED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Validator

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/validators/{validator_addr}`

*Validator queries validator info for given validator address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_addr|path|string|true|validator_addr defines the validator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

> The result from the above endpoint looks like this:

```json
{
  "delegation_responses": [
    {
      "delegation": {
        "delegator_address": "0x1234567890abcdef...",
        "validator_address": "0x1234567890abcdef...",
        "shares": "shares..."
      },
      "balance": {
        "denom": "denom...",
        "amount": "1000"
      }
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```


*QueryValidatorResponse is response type for the Query/Validator RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» validator|object|false|none|validator defines the the validator info.|
|»» operator_address|string|false|none|operator_address defines the address of the validator's operator; bech encoded in JSON.|
|»» consensus_pubkey|object|false|none|consensus_pubkey is the consensus public key of the validator, as a Protobuf Any.|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» jailed|boolean|false|none|jailed defined whether the validator has been jailed from bonded status or not.|
|»» status|string|false|none|status is the validator status (bonded/unbonding/unbonded).|
|»» tokens|string|false|none|tokens define the delegated tokens (incl. self-delegation).|
|»» delegator_shares|string|false|none|delegator_shares defines total shares issued to a validator's delegators.|
|»» description|object|false|none|description defines the description terms for the validator.|
|»»» moniker|string|false|none|moniker defines a human-readable name for the validator.|
|»»» identity|string|false|none|identity defines an optional identity signature (ex. UPort or Keybase).|
|»»» website|string|false|none|website defines an optional website link.|
|»»» security_contact|string|false|none|security_contact defines an optional email for security contact.|
|»»» details|string|false|none|details define other optional details.|
|»» unbonding_height|string(int64)|false|none|unbonding_height defines, if unbonding, the height at which this validator has begun unbonding.|
|»» unbonding_time|string(date-time)|false|none|unbonding_time defines, if unbonding, the min time for the validator to complete unbonding.|
|»» commission|object|false|none|commission defines the commission parameters.|
|»»» commission_rates|object|false|none|commission_rates defines the initial commission rates to be used for creating a validator.|
|»»»» rate|string|false|none|rate is the commission rate charged to delegators, as a fraction.|
|»»»» max_rate|string|false|none|max_rate defines the maximum commission rate which validator can ever charge, as a fraction.|
|»»»» max_change_rate|string|false|none|max_change_rate defines the maximum daily increase of the validator commission, as a fraction.|
|»»» update_time|string(date-time)|false|none|update_time is the last time the commission rate was changed.|
|»» min_self_delegation|string|false|none|min_self_delegation is the validator's self declared minimum self delegation.|

#### Enumerated Values

|Property|Value|
|---|---|
|status|BOND_STATUS_UNSPECIFIED|
|status|BOND_STATUS_UNBONDED|
|status|BOND_STATUS_UNBONDING|
|status|BOND_STATUS_BONDED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## ValidatorDelegations

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/delegations \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/delegations', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/validators/{validator_addr}/delegations`

*ValidatorDelegations queries delegate info for given validator.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_addr|path|string|true|validator_addr defines the validator address to query for.|
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

> The result from the above endpoint looks like this:

```json
{
  "delegation_response": {
    "delegation": {
      "delegator_address": "0x1234567890abcdef...",
      "validator_address": "0x1234567890abcdef...",
      "shares": "shares..."
    },
    "balance": {
      "denom": "denom...",
      "amount": "1000"
    }
  }
}
```

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

*QueryValidatorDelegationsResponse is response type for the
Query/ValidatorDelegations RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» delegation_responses|[object]|false|none|none|
|»» delegation|object|false|none|Delegation represents the bond with tokens held by an account. It isowned by one delegator, and is associated with the voting power of onevalidator.|
|»»» delegator_address|string|false|none|delegator_address is the bech32-encoded address of the delegator.|
|»»» validator_address|string|false|none|validator_address is the bech32-encoded address of the validator.|
|»»» shares|string|false|none|shares define the delegation shares received.|
|»» balance|object|false|none|Coin defines a token with a denomination and an amount.NOTE: The amount field is an Int which implements the custom methodsignatures required by gogoproto.|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|
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

## Delegation

> Code samples

```shell
curl --request GET \

> The result from the above endpoint looks like this:

```json
{
  "unbond": {
    "delegator_address": "0x1234567890abcdef...",
    "validator_address": "0x1234567890abcdef...",
    "entries": [
      {
        "creation_height": "creation_height...",
        "completion_time": "completion_time...",
        "initial_balance": "initial_balance..."
      }
    ]
  }
}
```

  --url https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/delegations/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/delegations/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}`

*Delegation queries delegate info for given validator delegator pair.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_addr|path|string|true|validator_addr defines the validator address to query for.|
|delegator_addr|path|string|true|delegator_addr defines the delegator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDelegationResponse is response type for the Query/Delegation RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» delegation_response|object|false|none|delegation_responses defines the delegation info of a delegation.|
|»» delegation|object|false|none|Delegation represents the bond with tokens held by an account. It isowned by one delegator, and is associated with the voting power of onevalidator.|
|»»» delegator_address|string|false|none|delegator_address is the bech32-encoded address of the delegator.|
|»»» validator_address|string|false|none|validator_address is the bech32-encoded address of the validator.|
|»»» shares|string|false|none|shares define the delegation shares received.|
|»» balance|object|false|none|Coin defines a token with a denomination and an amount.NOTE: The amount field is an Int which implements the custom methodsignatures required by gogoproto.|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## UnbondingDelegation

> The result from the above endpoint looks like this:

```json
{
  "unbonding_responses": [
    {
      "delegator_address": "0x1234567890abcdef...",
      "validator_address": "0x1234567890abcdef...",
      "entries": [
        {
          "creation_height": "creation_height...",
          "completion_time": "completion_time...",
          "initial_balance": "initial_balance..."
        }
      ]
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```


> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/delegations/string/unbonding_delegation \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/delegations/string/unbonding_delegation', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation`

*UnbondingDelegation queries unbonding info for given validator delegator
pair.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_addr|path|string|true|validator_addr defines the validator address to query for.|
|delegator_addr|path|string|true|delegator_addr defines the delegator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDelegationResponse is response type for the Query/UnbondingDelegation
RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» unbond|object|false|none|unbond defines the unbonding information of a delegation.|
|»» delegator_address|string|false|none|delegator_address is the bech32-encoded address of the delegator.|
|»» validator_address|string|false|none|validator_address is the bech32-encoded address of the validator.|
|»» entries|[object]|false|none|entries are the unbonding delegation entries.unbonding delegation entries|
|»»» creation_height|string(int64)|false|none|creation_height is the height which the unbonding took place.|
|»»» completion_time|string(date-time)|false|none|completion_time is the unix time for unbonding completion.|
|»»» initial_balance|string|false|none|initial_balance defines the tokens initially scheduled to receive at completion.|
|»»» balance|string|false|none|balance defines the tokens to receive at completion.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## ValidatorUnbondingDelegations

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/unbonding_delegations \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/staking/v1beta1/validators/string/unbonding_delegations', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations`

*ValidatorUnbondingDelegations queries unbonding delegations of a validator.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_addr|path|string|true|validator_addr defines the validator address to query for.|
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

*QueryValidatorUnbondingDelegationsResponse is response type for the
Query/ValidatorUnbondingDelegations RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» unbonding_responses|[object]|false|none|none|
|»» delegator_address|string|false|none|delegator_address is the bech32-encoded address of the delegator.|
|»» validator_address|string|false|none|validator_address is the bech32-encoded address of the validator.|
|»» entries|[object]|false|none|entries are the unbonding delegation entries.unbonding delegation entries|
|»»» creation_height|string(int64)|false|none|creation_height is the height which the unbonding took place.|
|»»» completion_time|string(date-time)|false|none|completion_time is the unix time for unbonding completion.|
|»»» initial_balance|string|false|none|initial_balance defines the tokens initially scheduled to receive at completion.|
|»»» balance|string|false|none|balance defines the tokens to receive at completion.|
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
