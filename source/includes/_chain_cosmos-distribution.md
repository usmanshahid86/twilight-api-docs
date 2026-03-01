## Cosmos Distribution Module

## CommunityPool

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/community_pool \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/community_pool', {
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
  "pool": [
    {
      "denom": "denom...",
      "amount": "1000"
    }
  ]
}
```


`GET /cosmos/distribution/v1beta1/community_pool`

*CommunityPool queries the community pool coins.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryCommunityPoolResponse is the response type for the Query/CommunityPool
RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» pool|[object]|false|none|pool defines community pool's coins.|
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

## DelegationTotalRewards

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/rewards \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/rewards', {

> The result from the above endpoint looks like this:

```json
{
  "rewards": [
    {
      "validator_address": "0x1234567890abcdef...",
      "reward": [
        {
          "denom": "denom...",
          "amount": "1000"
        }
      ]
    }
  ],
  "total": [
    {
      "denom": "denom...",
      "amount": "1000"
    }
  ]
}
```

  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards`

*DelegationTotalRewards queries the total rewards accrued by a each
validator.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_address|path|string|true|delegator_address defines the delegator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDelegationTotalRewardsResponse is the response type for the
Query/DelegationTotalRewards RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» rewards|[object]|false|none|rewards defines all the rewards accrued by a delegator.|
|»» validator_address|string|false|none|none|
|»» reward|[object]|false|none|none|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|
|» total|[object]|false|none|total defines the sum of all the rewards.|
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

## DelegationRewards

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "rewards": [
    {
      "denom": "denom...",
      "amount": "1000"
    }
  ]
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/rewards/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/rewards/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/delegators/{delegator_address}/rewards/{validator_address}`

*DelegationRewards queries the total rewards accrued by a delegation.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_address|path|string|true|delegator_address defines the delegator address to query for.|
|validator_address|path|string|true|validator_address defines the validator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDelegationRewardsResponse is the response type for the
Query/DelegationRewards RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» rewards|[object]|false|none|rewards defines the rewards accrued by a delegation.|
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


> The result from the above endpoint looks like this:

```json
{
  "validators": []
}
```

> This operation does not require authentication

## DelegatorValidators

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/validators \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/validators', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/delegators/{delegator_address}/validators`

*DelegatorValidators queries the validators of a delegator.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_address|path|string|true|delegator_address defines the delegator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDelegatorValidatorsResponse is the response type for the
Query/DelegatorValidators RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» validators|[string]|false|none|validators defines the validators a delegator is delegating for.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "withdraw_address": "0x1234567890abcdef..."
}
```

|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## DelegatorWithdrawAddress

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/withdraw_address \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/delegators/string/withdraw_address', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/delegators/{delegator_address}/withdraw_address`

*DelegatorWithdrawAddress queries withdraw address of a delegator.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|delegator_address|path|string|true|delegator_address defines the delegator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDelegatorWithdrawAddressResponse is the response type for the
Query/DelegatorWithdrawAddress RPC method.*


> The result from the above endpoint looks like this:

```json
{
  "params": {
    "community_tax": "community_tax...",
    "base_proposer_reward": "base_proposer_reward...",
    "bonus_proposer_reward": "bonus_proposer_reward...",
    "withdraw_addr_enabled": true
  }
}
```

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» withdraw_address|string|false|none|withdraw_address defines the delegator address to query for.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
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
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/params`

*Params queries params of the distribution module.*

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
  "commission": {
    "commission": [
      {
        "denom": "denom...",
        "amount": "1000"
      }
    ]
  }
}
```


*QueryParamsResponse is the response type for the Query/Params RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» params|object|false|none|params defines the parameters of the module.|
|»» community_tax|string|false|none|none|
|»» base_proposer_reward|string|false|none|none|
|»» bonus_proposer_reward|string|false|none|none|
|»» withdraw_addr_enabled|boolean|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## ValidatorCommission

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/validators/string/commission \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/validators/string/commission', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/validators/{validator_address}/commission`

*ValidatorCommission queries accumulated commission for a validator.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_address|path|string|true|validator_address defines the validator address to query for.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|

> The result from the above endpoint looks like this:

```json
{
  "rewards": {
    "rewards": [
      {
        "denom": "denom...",
        "amount": "1000"
      }
    ]
  }
}
```

|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryValidatorCommissionResponse is the response type for the
Query/ValidatorCommission RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» commission|object|false|none|commission defines the commision the validator received.|
|»» commission|[object]|false|none|none|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## ValidatorOutstandingRewards

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/validators/string/outstanding_rewards \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/validators/string/outstanding_rewards', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/validators/{validator_address}/outstanding_rewards`

*ValidatorOutstandingRewards queries rewards of a validator address.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_address|path|string|true|validator_address defines the validator address to query for.|


> The result from the above endpoint looks like this:

```json
{
  "slashes": [
    {
      "validator_period": "1000000",
      "fraction": "fraction..."
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
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

*QueryValidatorOutstandingRewardsResponse is the response type for the
Query/ValidatorOutstandingRewards RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» rewards|object|false|none|ValidatorOutstandingRewards represents outstanding (un-withdrawn) rewardsfor a validator inexpensive to track, allows simple sanity checks.|
|»» rewards|[object]|false|none|none|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## ValidatorSlashes

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/distribution/v1beta1/validators/string/slashes \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/distribution/v1beta1/validators/string/slashes', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/distribution/v1beta1/validators/{validator_address}/slashes`

*ValidatorSlashes queries slash events of a validator.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validator_address|path|string|true|validator_address defines the validator address to query for.|
|starting_height|query|string(uint64)|false|starting_height defines the optional starting height to query the slashes.|
|ending_height|query|string(uint64)|false|starting_height defines the optional ending height to query the slashes.|
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

*QueryValidatorSlashesResponse is the response type for the
Query/ValidatorSlashes RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» slashes|[object]|false|none|slashes defines the slashes the validator received.|
|»» validator_period|string(uint64)|false|none|none|
|»» fraction|string|false|none|none|
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
