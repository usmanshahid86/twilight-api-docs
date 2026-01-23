# Twilight Chain API — Twilight_Bridge

## Query

## TwilightprojectNyksBridgeBroadcastTxRefund

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/broadcast_tx_refund/string/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/broadcast_tx_refund/{reserveId}/{roundId}`

*Queries a list of BroadcastTxRefund items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|
|roundId|path|string(uint64)|true|none|

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
|» broadcastRefundMsg|object|false|none|none|
|»» reserveId|string(uint64)|false|none|none|
|»» roundId|string(uint64)|false|none|none|
|»» signedRefundTx|string|false|none|none|
|»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeBroadcastTxRefundAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/broadcast_tx_refund_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/broadcast_tx_refund_all`

*Queries a list of BroadcastTxRefundAll items.*

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
|» BroadcastTxRefundMsg|[object]|false|none|none|
|»» 6. MsgBroadcastTxRefund|object|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» signedRefundTx|string|false|none|none|
|»»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeBroadcastTxSweep

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/broadcast_tx_sweep/string/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/broadcast_tx_sweep/{reserveId}/{roundId}`

*Queries a list of BroadcastTxSweep items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|
|roundId|path|string(uint64)|true|none|

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
|» broadcastSweepMsg|object|false|none|none|
|»» reserveId|string(uint64)|false|none|none|
|»» roundId|string(uint64)|false|none|none|
|»» signedSweepTx|string|false|none|none|
|»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeBroadcastTxSweepAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/broadcast_tx_sweep_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/broadcast_tx_sweep_all`

*Queries a list of BroadcastTxSweepAll items.*

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
|» BroadcastTxSweepMsg|[object]|false|none|none|
|»» 7. MsgBroadcastTxSweep|object|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» signedSweepTx|string|false|none|none|
|»»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeParams

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/params \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/params`

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
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeProposeRefundHashAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/propose_refund_hash_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/propose_refund_hash_all`

*Queries a list of ProposeRefundHashAll items.*

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
|» proposeRefundHashMsg|[object]|false|none|none|
|»» refundHash|string|false|none|none|
|»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeProposeSweepAddress

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/propose_sweep_address/string/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/propose_sweep_address/{reserveId}/{roundId}`

*Queries a list of ProposeSweepAddress items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|
|roundId|path|string(uint64)|true|none|

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
|» proposeSweepAddressMsg|object|false|none|none|
|»» btcAddress|string|false|none|none|
|»» btcScript|string|false|none|none|
|»» reserveId|string(uint64)|false|none|none|
|»» roundId|string(uint64)|false|none|none|
|»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeProposeSweepAddressesAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/propose_sweep_addresses_all/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/propose_sweep_addresses_all/{limit}`

*Queries a list of ProposeSweepAddressesAll items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|path|string(uint64)|true|none|

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
|» proposeSweepAddressMsgs|[object]|false|none|none|
|»» Sweep messages in order
1. MsgProposeSweepAddress|object|false|none|none|
|»»» btcAddress|string|false|none|none|
|»»» btcScript|string|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeRegisteredBtcDepositAddress

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/registered_btc_deposit_address/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/registered_btc_deposit_address/{depositAddress}`

*Queries a list of RegisteredBtcDepositAddress items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|depositAddress|path|string|true|none|

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
|» depositAddress|string|false|none|none|
|» twilightDepositAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeRegisteredBtcDepositAddressByTwilightAddress

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/registered_btc_deposit_address_by_twilight_address/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/registered_btc_deposit_address_by_twilight_address/{twilightDepositAddress}`

*Queries a list of RegisteredBtcDepositAddressByTwilightAddress items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|twilightDepositAddress|path|string|true|none|

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
|» depositAddress|string|false|none|none|
|» twilightDepositAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeRegisteredBtcDepositAddresses

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/registered_btc_deposit_addresses \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/registered_btc_deposit_addresses`

*Queries a list of RegisteredBtcDepositAddresses items.*

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
|»» btcDepositAddress|string|false|none|none|
|»» btcSatoshiTestAmount|string(uint64)|false|none|none|
|»» twilightStakingAmount|string(uint64)|false|none|none|
|»» twilightAddress|string|false|none|none|
|»» isConfirmed|boolean|false|none|none|
|»» CreationTwilightBlockHeight|string(int64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeRegisteredJudgeAddressByValidatorAddress

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/registered_judge_address_by_validator_address/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/registered_judge_address_by_validator_address/{validatorAddress}`

*Queries a list of RegisteredJudgeAddressByValidatorAddress items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|validatorAddress|path|string|true|none|

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
|» judgeAddress|string|false|none|none|
|» numOfSigners|string(uint64)|false|none|none|
|» threshold|string(uint64)|false|none|none|
|» signerApplicationFee|string(uint64)|false|none|none|
|» arbitraryData|string|false|none|none|
|» validatorAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeRegisteredJudges

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/registered_judges \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/registered_judges`

*Queries a list of RegisteredJudges items.*

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
|» Judges|[object]|false|none|none|
|»» judgeAddress|string|false|none|none|
|»» numOfSigners|string(uint64)|false|none|none|
|»» threshold|string(uint64)|false|none|none|
|»» signerApplicationFee|string(uint64)|false|none|none|
|»» fragmentFeeBips|string(uint64)|false|none|none|
|»» arbitraryData|string|false|none|none|
|»» validatorAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeRegisteredReserveAddresses

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/registered_reserve_addresses \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/registered_reserve_addresses`

*Queries a list of RegisteredReserveAddresses items.*

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
|»» fragmentId|string(uint64)|false|none|none|
|»» reserveScript|string|false|none|none|
|»» reserveAddress|string|false|none|none|
|»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeSignRefund

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/sign_refund/string/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/sign_refund/{reserveId}/{roundId}`

*Queries a list of SignRefund items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|
|roundId|path|string(uint64)|true|none|

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
|» signRefundMsg|[object]|false|none|none|
|»» 4. MsgSignRefund|object|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» signerPublicKey|string|false|none|none|
|»»» refundSignature|[string]|false|none|none|
|»»» signerAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeSignRefundAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/sign_refund_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/sign_refund_all`

*Queries a list of SignRefundAll items.*

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
|» signRefundMsg|[object]|false|none|none|
|»» 4. MsgSignRefund|object|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» signerPublicKey|string|false|none|none|
|»»» refundSignature|[string]|false|none|none|
|»»» signerAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeSignSweep

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/sign_sweep/string/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/sign_sweep/{reserveId}/{roundId}`

*Queries a list of SignSweep items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|
|roundId|path|string(uint64)|true|none|

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
|» signSweepMsg|[object]|false|none|none|
|»» 5. MsgSignSweep|object|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» signerPublicKey|string|false|none|none|
|»»» sweepSignature|[string]|false|none|none|
|»»» signerAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeSignSweepAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/sign_sweep_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/sign_sweep_all`

*Queries a list of SignSweepAll items.*

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
|» signSweepMsg|[object]|false|none|none|
|»» 5. MsgSignSweep|object|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» signerPublicKey|string|false|none|none|
|»»» sweepSignature|[string]|false|none|none|
|»»» signerAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeUnsignedTxRefund

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/unsigned_tx_refund/string/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/unsigned_tx_refund/{reserveId}/{roundId}`

*Queries a list of UnsignedTxRefund items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|
|roundId|path|string(uint64)|true|none|

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
|» unsignedTxRefundMsg|object|false|none|none|
|»» reserveId|string(uint64)|false|none|none|
|»» roundId|string(uint64)|false|none|none|
|»» btcUnsignedRefundTx|string|false|none|none|
|»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeUnsignedTxRefundAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/unsigned_tx_refund_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/unsigned_tx_refund_all`

*Queries a list of UnsignedTxRefundAll items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string(uint64)|false|none|

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
|» unsignedTxRefundMsgs|[object]|false|none|none|
|»» 3. MsgUnsignedTxRefund|object|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» btcUnsignedRefundTx|string|false|none|none|
|»»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeUnsignedTxSweep

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/unsigned_tx_sweep/string/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/unsigned_tx_sweep/{reserveId}/{roundId}`

*Queries a list of UnsignedTxSweep items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|
|roundId|path|string(uint64)|true|none|

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
|» unsignedTxSweepMsg|object|false|none|none|
|»» txId|string|false|none|none|
|»» btcUnsignedSweepTx|string|false|none|none|
|»» reserveId|string(uint64)|false|none|none|
|»» roundId|string(uint64)|false|none|none|
|»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeUnsignedTxSweepAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/unsigned_tx_sweep_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/unsigned_tx_sweep_all`

*Queries a list of UnsignedTxSweepAll items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string(uint64)|false|none|

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
|» unsignedTxSweepMsgs|[object]|false|none|none|
|»» 2. MsgUnsignedTxSweep|object|false|none|none|
|»»» txId|string|false|none|none|
|»»» btcUnsignedSweepTx|string|false|none|none|
|»»» reserveId|string(uint64)|false|none|none|
|»»» roundId|string(uint64)|false|none|none|
|»»» judgeAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## TwilightprojectNyksBridgeWithdrawBtcRequestAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/bridge/withdraw_btc_request_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/bridge/withdraw_btc_request_all`

*Queries a list of WithdrawBtcRequestAll items.*

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
|» withdrawRequest|[object]|false|none|none|
|»» Chain creates an internal mapping with identifier and bool confirmed|object|false|none|none|
|»»» withdrawIdentifier|integer(int64)|false|none|none|
|»»» withdrawAddress|string|false|none|none|
|»»» withdrawReserveId|string(uint64)|false|none|none|
|»»» withdrawAmount|string(uint64)|false|none|none|
|»»» twilightAddress|string|false|none|none|
|»»» isConfirmed|boolean|false|none|none|
|»»» CreationTwilightBlockHeight|string(int64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication
