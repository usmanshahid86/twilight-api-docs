# Nyks Tendermint Queries

## TendermintSpnMonitoringpConnectionChannelID

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/tendermint/spn/monitoringp/connection_channel_id \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/tendermint/spn/monitoringp/connection_channel_id', {
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
  "ConnectionChannelID": {
    "channelID": "0x1234567890abcdef..."
  }
}
```


`GET /tendermint/spn/monitoringp/connection_channel_id`

*Queries a ConnectionChannelID by index.*

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
|» ConnectionChannelID|object|false|none|none|
|»» channelID|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TendermintSpnMonitoringpConsumerClientID

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/tendermint/spn/monitoringp/consumer_client_id \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/tendermint/spn/monitoringp/consumer_client_id', {

> The result from the above endpoint looks like this:

```json
{
  "ConsumerClientID": {
    "clientID": "0x1234567890abcdef..."
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

`GET /tendermint/spn/monitoringp/consumer_client_id`

*Queries a ConsumerClientID by index.*

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
|» ConsumerClientID|object|false|none|none|
|»» clientID|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TendermintSpnMonitoringpMonitoringInfo

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "MonitoringInfo": {
    "transmitted": true,
    "signatureCounts": {
      "blockCount": "1000000",
      "counts": [
        {
          "opAddress": "0x1234567890abcdef...",
          "RelativeSignatures": "RelativeSignatures..."
        }
      ]
    }
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/tendermint/spn/monitoringp/monitoring_info \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/tendermint/spn/monitoringp/monitoring_info', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /tendermint/spn/monitoringp/monitoring_info`

*Queries a MonitoringInfo by index.*

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
|» MonitoringInfo|object|false|none|none|
|»» transmitted|boolean|false|none|none|
|»» signatureCounts|object|false|none|none|
|»»» blockCount|string(uint64)|false|none|none|
|»»» counts|[object]|false|none|none|
|»»»» SignatureCount contains information of signature reporting for one specific validator with consensus address
RelativeSignatures is the sum of all signatures relative to the validator set size|object|false|none|none|
|»»»»» opAddress|string|false|none|none|
|»»»»» RelativeSignatures|string|false|none|none|

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
  "params": {
    "lastBlockHeight": "lastBlockHeight...",
    "consumerChainID": "0x1234567890abcdef...",
    "consumerConsensusState": {
      "nextValidatorsHash": "0x1234567890abcdef...",
      "timestamp": "timestamp...",
      "root": {
        "hash": "0x1234567890abcdef..."
      }
    },
    "consumerUnbondingPeriod": "consumerUnbondingPeriod...",
    "consumerRevisionHeight": "1000000"
  }
}
```

> This operation does not require authentication

## TendermintSpnMonitoringpParams

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/tendermint/spn/monitoringp/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/tendermint/spn/monitoringp/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /tendermint/spn/monitoringp/params`

*Params queries the parameters of the module.*

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
|» params|object|false|none|Params defines the parameters for the module.|
|»» lastBlockHeight|string(int64)|false|none|none|
|»» consumerChainID|string|false|none|none|
|»» consumerConsensusState|object|false|none|none|
|»»» nextValidatorsHash|string|false|none|none|
|»»» timestamp|string|false|none|none|
|»»» root|object|false|none|none|
|»»»» hash|string|false|none|none|
|»» consumerUnbondingPeriod|string(int64)|false|none|none|
|»» consumerRevisionHeight|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication
