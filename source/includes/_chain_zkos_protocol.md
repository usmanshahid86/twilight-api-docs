# Twilight Modules

## ZKOS Module (Chain REST API)

<h1 id="http-api-console-twilight-zkos">HTTP API Console — twilight-zkos v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="http-api-console-twilight-zkos-query">Query</h1>

## TwilightprojectNyksZkosMintOrBurnTradingBtc

<a id="opIdTwilightprojectNyksZkosMintOrBurnTradingBtc"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /twilight-project/nyks/zkos/mint_or_burn_trading_btc/{twilightAddress} \
  -H 'Accept: */*'

```

`GET /twilight-project/nyks/zkos/mint_or_burn_trading_btc/{twilightAddress}`

*Queries a list of MintOrBurnTradingBtc items.*

<h3 id="twilightprojectnykszkosmintorburntradingbtc-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|twilightAddress|path|string|true|none|

> Example responses

> 200 Response

<h3 id="twilightprojectnykszkosmintorburntradingbtc-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

<h3 id="twilightprojectnykszkosmintorburntradingbtc-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» MintOrBurnTradingBtc|[object]|false|none|none|
|»» mintOrBurn|boolean|false|none|none|
|»» btcValue|string(uint64)|false|none|none|
|»» qqAccount|string|false|none|none|
|»» encryptScalar|string|false|none|none|
|»» twilightAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## TwilightprojectNyksZkosParams

<a id="opIdTwilightprojectNyksZkosParams"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /twilight-project/nyks/zkos/params \
  -H 'Accept: */*'

```

`GET /twilight-project/nyks/zkos/params`

*Parameters queries the parameters of the module.*

> Example responses

> 200 Response

<h3 id="twilightprojectnykszkosparams-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

<h3 id="twilightprojectnykszkosparams-responseschema">Response Schema</h3>

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

<aside class="success">
This operation does not require authentication
</aside>

## TwilightprojectNyksZkosTransferTx

<a id="opIdTwilightprojectNyksZkosTransferTx"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /twilight-project/nyks/zkos/transfer_tx/{txId} \
  -H 'Accept: */*'

```

`GET /twilight-project/nyks/zkos/transfer_tx/{txId}`

*Queries a list of TransferTx items.*

<h3 id="twilightprojectnykszkostransfertx-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|none|

> Example responses

> 200 Response

<h3 id="twilightprojectnykszkostransfertx-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

<h3 id="twilightprojectnykszkostransfertx-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» TransferTx|object|false|none|none|
|»» txId|string|false|none|none|
|»» txByteCode|string|false|none|none|
|»» txFee|string(uint64)|false|none|none|
|»» zkOracleAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

