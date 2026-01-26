# Twilight Chain API 

## Cosmos Slashing

## Params

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/slashing/v1beta1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/slashing/v1beta1/params', {
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
  "params": {
    "signed_blocks_window": "signed_blocks_window...",
    "min_signed_per_window": "min_signed_per_window...",
    "downtime_jail_duration": "downtime_jail_duration...",
    "slash_fraction_double_sign": "slash_fraction_double_sign...",
    "slash_fraction_downtime": "slash_fraction_downtime..."
  }
}
```


`GET /cosmos/slashing/v1beta1/params`

*Params queries the parameters of slashing module*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryParamsResponse is the response type for the Query/Params RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» params|object|false|none|Params represents the parameters used for by the slashing module.|
|»» signed_blocks_window|string(int64)|false|none|none|
|»» min_signed_per_window|string(byte)|false|none|none|
|»» downtime_jail_duration|string|false|none|none|
|»» slash_fraction_double_sign|string(byte)|false|none|none|
|»» slash_fraction_downtime|string(byte)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## SigningInfos

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/slashing/v1beta1/signing_infos \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/slashing/v1beta1/signing_infos', {

> The result from the above endpoint looks like this:

```json
{
  "info": [
    {
      "address": "0x1234567890abcdef...",
      "start_height": "start_height...",
      "index_offset": "index_offset..."
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

`GET /cosmos/slashing/v1beta1/signing_infos`

*SigningInfos queries signing info of all validators*

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

*QuerySigningInfosResponse is the response type for the Query/SigningInfos RPC
method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» info|[object]|false|none|none|
|»» address|string|false|none|none|
|»» start_height|string(int64)|false|none|none|
|»» index_offset|string(int64)|false|none|Index which is incremented each time the validator was a bondedin a block and may have signed a precommit or not. This in conjunction with the`SignedBlocksWindow` param determines the index in the `MissedBlocksBitArray`.|
|»» jailed_until|string(date-time)|false|none|Timestamp until which the validator is jailed due to liveness downtime.|
|»» tombstoned|boolean|false|none|Whether or not a validator has been tombstoned (killed out of validator set). It is setonce the validator commits an equivocation or for any other configured misbehiavor.|
|»» missed_blocks_counter|string(int64)|false|none|A counter kept to avoid unnecessary array reads.Note that `Sum(MissedBlocksBitArray)` always equals `MissedBlocksCounter`.|
|» pagination|object|false|none|PageResponse is to be embedded in gRPC response messages where thecorresponding request message has used PageRequest. message SomeResponse {         repeated Bar results = 1;         PageResponse page = 2; }|
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

## SigningInfo

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "val_signing_info": {
    "address": "0x1234567890abcdef...",
    "start_height": "start_height...",
    "index_offset": "index_offset...",
    "jailed_until": "jailed_until...",
    "tombstoned": true,
    "missed_blocks_counter": "missed_blocks_counter..."
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/slashing/v1beta1/signing_infos/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/slashing/v1beta1/signing_infos/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/slashing/v1beta1/signing_infos/{cons_address}`

*SigningInfo queries the signing info of given cons address*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cons_address|path|string|true|cons_address is the address to query signing info of|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QuerySigningInfoResponse is the response type for the Query/SigningInfo RPC
method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» val_signing_info|object|false|none|ValidatorSigningInfo defines a validator's signing info for monitoring theirliveness activity.|
|»» address|string|false|none|none|
|»» start_height|string(int64)|false|none|none|
|»» index_offset|string(int64)|false|none|Index which is incremented each time the validator was a bondedin a block and may have signed a precommit or not. This in conjunction with the`SignedBlocksWindow` param determines the index in the `MissedBlocksBitArray`.|
|»» jailed_until|string(date-time)|false|none|Timestamp until which the validator is jailed due to liveness downtime.|
|»» tombstoned|boolean|false|none|Whether or not a validator has been tombstoned (killed out of validator set). It is setonce the validator commits an equivocation or for any other configured misbehiavor.|
|»» missed_blocks_counter|string(int64)|false|none|A counter kept to avoid unnecessary array reads.Note that `Sum(MissedBlocksBitArray)` always equals `MissedBlocksCounter`.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication
