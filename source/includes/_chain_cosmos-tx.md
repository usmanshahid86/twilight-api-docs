## Cosmos Tx - Service Module

## Simulate

> Code samples

```shell
curl --request POST \
  --url https://lcd.twilight.org/cosmos/tx/v1beta1/simulate \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data '{"tx":{"body":{"messages":[{"@type":"string","property1":null,"property2":null}],"memo":"string","timeout_height":"string","extension_options":[{"@type":"string","property1":null,"property2":null}],"non_critical_extension_options":[{"@type":"string","property1":null,"property2":null}]},"auth_info":{"signer_infos":[{"public_key":{"@type":"string","property1":null,"property2":null},"mode_info":{"single":{"mode":"SIGN_MODE_UNSPECIFIED"},"multi":{"bitarray":{"extra_bits_stored":0,"elems":"string"},"mode_infos":[{}]}},"sequence":"string"}],"fee":{"amount":[{"denom":"string","amount":"string"}],"gas_limit":"string","payer":"string","granter":"string"}},"signatures":["string"]},"tx_bytes":"string"}'
```

> The result from the above endpoint looks like this:

```json
{
  "gas_info": {
    "gas_wanted": "1000000",
    "gas_used": "1000000"
  },
  "result": {
    "data": "data...",
    "log": "log...",
    "events": [
      {
        "type": "type...",
        "attributes": [
          {
            "key": "key...",
            "value": "1000",
            "index": true
          }
        ]
      }
    ]
  }
}
```


```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/tx/v1beta1/simulate', {
  method: 'POST',
  headers: {
    'Accept': '*/*',
    'Content-Type': 'application/json'
  }
});
const data = await response.json();
console.log(data);
```

`POST /cosmos/tx/v1beta1/simulate`

*Simulate simulates executing a transaction for estimating gas usage.*

> Body parameter

```json
{
  "tx": {
    "body": {
      "messages": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ],
      "memo": "string",
      "timeout_height": "string",
      "extension_options": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ],
      "non_critical_extension_options": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ]
    },
    "auth_info": {
      "signer_infos": [
        {
          "public_key": {
            "@type": "string",
            "property1": null,
            "property2": null
          },
          "mode_info": {
            "single": {
              "mode": "SIGN_MODE_UNSPECIFIED"
            },
            "multi": {
              "bitarray": {
                "extra_bits_stored": 0,
                "elems": "string"
              },
              "mode_infos": [
                {}
              ]
            }
          },
          "sequence": "string"
        }
      ],
      "fee": {
        "amount": [
          {
            "denom": "string",
            "amount": "string"
          }
        ],
        "gas_limit": "string",
        "payer": "string",
        "granter": "string"
      }
    },
    "signatures": [
      "string"
    ]
  },
  "tx_bytes": "string"
}
```

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[cosmos.tx.v1beta1.SimulateRequest](#schemacosmos.tx.v1beta1.simulaterequest)|true|SimulateRequest is the request type for the Service.Simulate|

#### Detailed descriptions

**body**: SimulateRequest is the request type for the Service.Simulate
RPC method.

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*SimulateResponse is the response type for the
Service.SimulateRPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» gas_info|object|false|none|gas_info is the information about gas used in the simulation.|
|»» gas_wanted|string(uint64)|false|none|GasWanted is the maximum units of work we allow this tx to perform.|
|»» gas_used|string(uint64)|false|none|GasUsed is the amount of gas actually consumed.|
|» result|object|false|none|result is the result of the simulation.|
|»» data|string(byte)|false|none|Data is any data returned from message or handler execution. It MUST belength prefixed in order to separate data from multiple message executions.|
|»» log|string|false|none|Log contains the log information from message or handler execution.|
|»» events|[object]|false|none|Events contains a slice of Event objects that were emitted during messageor handler execution.|
|»»» type|string|false|none|none|
|»»» attributes|[object]|false|none|none|
|»»»» key|string(byte)|false|none|none|
|»»»» value|string(byte)|false|none|none|
|»»»» index|boolean|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## GetTxsEvent

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/tx/v1beta1/txs \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/tx/v1beta1/txs', {

> The result from the above endpoint looks like this:

```json
{
  "status": "success",
  "data": {}
}
```

  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/tx/v1beta1/txs`

*GetTxsEvent fetches txs by event.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|events|query|array[string]|false|events is the list of transaction event type.|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|
|pagination.reverse|query|boolean|false|reverse is set to true if results are to be returned in the descending order.|
|order_by|query|string|false| - ORDER_BY_UNSPECIFIED: ORDER_BY_UNSPECIFIED specifies an unknown sorting order. OrderBy defaults to ASC in this case.|

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

**order_by**:  - ORDER_BY_UNSPECIFIED: ORDER_BY_UNSPECIFIED specifies an unknown sorting order. OrderBy defaults to ASC in this case.
 - ORDER_BY_ASC: ORDER_BY_ASC defines ascending order
 - ORDER_BY_DESC: ORDER_BY_DESC defines descending order

#### Enumerated Values

|Parameter|Value|
|---|---|
|order_by|ORDER_BY_UNSPECIFIED|
|order_by|ORDER_BY_ASC|
|order_by|ORDER_BY_DESC|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|[cosmos.tx.v1beta1.GetTxsEventResponse](#schemacosmos.tx.v1beta1.gettxseventresponse)|
|default|Default|An unexpected error response.|Inline|

### Response Schema

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
  "tx_response": {
    "height": "height...",
    "txhash": "0x1234567890abcdef...",
    "codespace": "0xabcdef1234567890...",
    "code": 0,
    "data": "data...",
    "raw_log": "raw_log...",
    "logs": [
      {
        "msg_index": 0,
        "log": "log...",
        "events": [
          {
            "type": "type...",
            "attributes": [
              {
                "key": "key...",
                "value": "1000"
              }
            ]
          }
        ]
      }
    ],
    "info": "info...",
    "gas_wanted": "gas_wanted...",
    "gas_used": "gas_used...",
    "tx": {
      "@type": "@type..."
    },
    "timestamp": "timestamp...",
    "events": [
      {
        "type": "type...",
        "attributes": [
          {
            "key": "key...",
            "value": "1000",
            "index": true
          }
        ]
      }
    ]
  }
}
```


> This operation does not require authentication

## BroadcastTx

> Code samples

```shell
curl --request POST \
  --url https://lcd.twilight.org/cosmos/tx/v1beta1/txs \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data '{"tx_bytes":"string","mode":"BROADCAST_MODE_UNSPECIFIED"}'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/tx/v1beta1/txs', {
  method: 'POST',
  headers: {
    'Accept': '*/*',
    'Content-Type': 'application/json'
  }
});
const data = await response.json();
console.log(data);
```

`POST /cosmos/tx/v1beta1/txs`

*BroadcastTx broadcast transaction.*

> Body parameter

```json
{
  "tx_bytes": "string",
  "mode": "BROADCAST_MODE_UNSPECIFIED"
}
```

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|BroadcastTxRequest is the request type for the Service.BroadcastTxRequest|
|» tx_bytes|body|string(byte)|false|tx_bytes is the raw transaction.|
|» mode|body|string|false|BroadcastMode specifies the broadcast mode for the TxService.Broadcast RPC method.|

#### Detailed descriptions

**body**: BroadcastTxRequest is the request type for the Service.BroadcastTxRequest
RPC method.

**» mode**: BroadcastMode specifies the broadcast mode for the TxService.Broadcast RPC method.

 - BROADCAST_MODE_UNSPECIFIED: zero-value for mode ordering
 - BROADCAST_MODE_BLOCK: BROADCAST_MODE_BLOCK defines a tx broadcasting mode where the client waits for
the tx to be committed in a block.
 - BROADCAST_MODE_SYNC: BROADCAST_MODE_SYNC defines a tx broadcasting mode where the client waits for
a CheckTx execution response only.
 - BROADCAST_MODE_ASYNC: BROADCAST_MODE_ASYNC defines a tx broadcasting mode where the client returns
immediately.

#### Enumerated Values

|Parameter|Value|
|---|---|
|» mode|BROADCAST_MODE_UNSPECIFIED|
|» mode|BROADCAST_MODE_BLOCK|
|» mode|BROADCAST_MODE_SYNC|
|» mode|BROADCAST_MODE_ASYNC|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*BroadcastTxResponse is the response type for the
Service.BroadcastTx method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tx_response|object|false|none|tx_response is the queried TxResponses.|
|»» height|string(int64)|false|none|none|
|»» txhash|string|false|none|The transaction hash.|
|»» codespace|string|false|none|none|
|»» code|integer(int64)|false|none|Response code.|
|»» data|string|false|none|Result bytes, if any.|
|»» raw_log|string|false|none|The output of the application's logger (raw string). May benon-deterministic.|
|»» logs|[object]|false|none|The output of the application's logger (typed). May be non-deterministic.|
|»»» msg_index|integer(int64)|false|none|none|
|»»» log|string|false|none|none|
|»»» events|[object]|false|none|Events contains a slice of Event objects that were emitted during someexecution.|
|»»»» type|string|false|none|none|
|»»»» attributes|[object]|false|none|none|
|»»»»» key|string|false|none|none|
|»»»»» value|string|false|none|none|
|»» info|string|false|none|Additional information. May be non-deterministic.|
|»» gas_wanted|string(int64)|false|none|Amount of gas requested for transaction.|
|»» gas_used|string(int64)|false|none|Amount of gas consumed by transaction.|
|»» tx|object|false|none|The request transaction bytes.|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» timestamp|string|false|none|Time of the previous block. For heights > 1, it's the weighted median ofthe timestamps of the valid votes in the block.LastCommit. For height == 1,it's genesis time.|
|»» events|[object]|false|none|Events defines all the events emitted by processing a transaction. Note,these events include those emitted by processing all the messages and thoseemitted from the ante handler. Whereas Logs contains the events, withadditional metadata, emitted only by processing the messages.Since: cosmos-sdk 0.42.11, 0.44.5, 0.45|
|»»» type|string|false|none|none|
|»»» attributes|[object]|false|none|none|
|»»»» key|string(byte)|false|none|none|
|»»»» value|string(byte)|false|none|none|
|»»»» index|boolean|false|none|none|

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
  "status": "success",
  "data": {}
}
```

> This operation does not require authentication

## GetBlockWithTxs

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/tx/v1beta1/txs/block/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/tx/v1beta1/txs/block/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/tx/v1beta1/txs/block/{height}`

*GetBlockWithTxs fetches a block with decoded txs.*

Since: cosmos-sdk 0.45.2

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|height|path|string(int64)|true|height is the height of the block to query.|
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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|[cosmos.tx.v1beta1.GetBlockWithTxsResponse](#schemacosmos.tx.v1beta1.getblockwithtxsresponse)|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "status": "success",
  "data": {}
}
```

|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## GetTx

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/tx/v1beta1/txs/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/tx/v1beta1/txs/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/tx/v1beta1/txs/{hash}`

*GetTx fetches a tx by hash.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hash|path|string|true|hash is the tx hash to query, encoded as a hex string.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|[cosmos.tx.v1beta1.GetTxResponse](#schemacosmos.tx.v1beta1.gettxresponse)|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Schemas

## cosmos.tx.v1beta1.AuthInfo

```json
{
  "signer_infos": [
    {
      "public_key": {
        "@type": "string",
        "property1": null,
        "property2": null
      },
      "mode_info": {
        "single": {
          "mode": "SIGN_MODE_UNSPECIFIED"
        },
        "multi": {
          "bitarray": {
            "extra_bits_stored": 0,
            "elems": "string"
          },
          "mode_infos": [
            {}
          ]
        }
      },
      "sequence": "string"
    }
  ],
  "fee": {
    "amount": [
      {
        "denom": "string",
        "amount": "string"
      }
    ],
    "gas_limit": "string",
    "payer": "string",
    "granter": "string"
  }
}

```

AuthInfo describes the fee and signer modes that are used to sign a
transaction.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|signer_infos|[[cosmos.tx.v1beta1.SignerInfo](#schemacosmos.tx.v1beta1.signerinfo)]|false|none|signer_infos defines the signing modes for the required signers. The numberand order of elements must match the required signers from TxBody'smessages. The first element is the primary signer and the one which paysthe fee.|
|fee|object|false|none|Fee is the fee and gas limit for the transaction. The first signer is theprimary signer and the one which pays the fee. The fee can be calculatedbased on the cost of evaluating the body and doing signature verificationof the signers. This can be estimated via simulation.|
|» amount|[object]|false|none|none|
|»» denom|string|false|none|none|
|»» amount|string|false|none|none|
|» gas_limit|string(uint64)|false|none|none|
|» payer|string|false|none|if unset, the first signer is responsible for paying the fees. If set, the specified account must pay the fees.the payer must be a tx signer (and thus have signed this field in AuthInfo).setting this field does *not* change the ordering of required signers for the transaction.|
|» granter|string|false|none|none|

## cosmos.tx.v1beta1.GetBlockWithTxsResponse

```json
{
  "txs": [
    {
      "body": {
        "messages": [
          {
            "@type": "string",
            "property1": null,
            "property2": null
          }
        ],
        "memo": "string",
        "timeout_height": "string",
        "extension_options": [
          {
            "@type": "string",
            "property1": null,
            "property2": null
          }
        ],
        "non_critical_extension_options": [
          {
            "@type": "string",
            "property1": null,
            "property2": null
          }
        ]
      },
      "auth_info": {
        "signer_infos": [
          {
            "public_key": {
              "@type": "string",
              "property1": null,
              "property2": null
            },
            "mode_info": {
              "single": {
                "mode": "SIGN_MODE_UNSPECIFIED"
              },
              "multi": {
                "bitarray": {
                  "extra_bits_stored": 0,
                  "elems": "string"
                },
                "mode_infos": [
                  {}
                ]
              }
            },
            "sequence": "string"
          }
        ],
        "fee": {
          "amount": [
            {
              "denom": "string",
              "amount": "string"
            }
          ],
          "gas_limit": "string",
          "payer": "string",
          "granter": "string"
        }
      },
      "signatures": [
        "string"
      ]
    }
  ],
  "block_id": {
    "hash": "string",
    "part_set_header": {
      "total": 0,
      "hash": "string"
    }
  },
  "block": {
    "header": {
      "version": {
        "block": "string",
        "app": "string"
      },
      "chain_id": "string",
      "height": "string",
      "time": "2019-08-24T14:15:22Z",
      "last_block_id": {
        "hash": "string",
        "part_set_header": {
          "total": 0,
          "hash": "string"
        }
      },
      "last_commit_hash": "string",
      "data_hash": "string",
      "validators_hash": "string",
      "next_validators_hash": "string",
      "consensus_hash": "string",
      "app_hash": "string",
      "last_results_hash": "string",
      "evidence_hash": "string",
      "proposer_address": "string"
    },
    "data": {
      "txs": [
        "string"
      ]
    },
    "evidence": {
      "evidence": [
        {
          "duplicate_vote_evidence": {
            "vote_a": {
              "type": "SIGNED_MSG_TYPE_UNKNOWN",
              "height": "string",
              "round": 0,
              "block_id": {
                "hash": "string",
                "part_set_header": {
                  "total": 0,
                  "hash": "string"
                }
              },
              "timestamp": "2019-08-24T14:15:22Z",
              "validator_address": "string",
              "validator_index": 0,
              "signature": "string"
            },
            "vote_b": {
              "type": "SIGNED_MSG_TYPE_UNKNOWN",
              "height": "string",
              "round": 0,
              "block_id": {
                "hash": "string",
                "part_set_header": {
                  "total": 0,
                  "hash": "string"
                }
              },
              "timestamp": "2019-08-24T14:15:22Z",
              "validator_address": "string",
              "validator_index": 0,
              "signature": "string"
            },
            "total_voting_power": "string",
            "validator_power": "string",
            "timestamp": "2019-08-24T14:15:22Z"
          },
          "light_client_attack_evidence": {
            "conflicting_block": {
              "signed_header": {
                "header": {
                  "version": {
                    "block": "string",
                    "app": "string"
                  },
                  "chain_id": "string",
                  "height": "string",
                  "time": "2019-08-24T14:15:22Z",
                  "last_block_id": {
                    "hash": "string",
                    "part_set_header": {}
                  },
                  "last_commit_hash": "string",
                  "data_hash": "string",
                  "validators_hash": "string",
                  "next_validators_hash": "string",
                  "consensus_hash": "string",
                  "app_hash": "string",
                  "last_results_hash": "string",
                  "evidence_hash": "string",
                  "proposer_address": "string"
                },
                "commit": {
                  "height": "string",
                  "round": 0,
                  "block_id": {
                    "hash": "string",
                    "part_set_header": {}
                  },
                  "signatures": [
                    {}
                  ]
                }
              },
              "validator_set": {
                "validators": [
                  {
                    "address": "string",
                    "pub_key": {},
                    "voting_power": "string",
                    "proposer_priority": "string"
                  }
                ],
                "proposer": {
                  "address": "string",
                  "pub_key": {
                    "ed25519": "string",
                    "secp256k1": "string"
                  },
                  "voting_power": "string",
                  "proposer_priority": "string"
                },
                "total_voting_power": "string"
              }
            },
            "common_height": "string",
            "byzantine_validators": [
              {
                "address": "string",
                "pub_key": {
                  "ed25519": "string",
                  "secp256k1": "string"
                },
                "voting_power": "string",
                "proposer_priority": "string"
              }
            ],
            "total_voting_power": "string",
            "timestamp": "2019-08-24T14:15:22Z"
          }
        }
      ]
    },
    "last_commit": {
      "height": "string",
      "round": 0,
      "block_id": {
        "hash": "string",
        "part_set_header": {
          "total": 0,
          "hash": "string"
        }
      },
      "signatures": [
        {
          "block_id_flag": "BLOCK_ID_FLAG_UNKNOWN",
          "validator_address": "string",
          "timestamp": "2019-08-24T14:15:22Z",
          "signature": "string"
        }
      ]
    }
  },
  "pagination": {
    "next_key": "string",
    "total": "string"
  }
}

```

GetBlockWithTxsResponse is the response type for the Service.GetBlockWithTxs method.

Since: cosmos-sdk 0.45.2

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txs|[[cosmos.tx.v1beta1.Tx](#schemacosmos.tx.v1beta1.tx)]|false|none|txs are the transactions in the block.|
|block_id|object|false|none|none|
|» hash|string(byte)|false|none|none|
|» part_set_header|object|false|none|none|
|»» total|integer(int64)|false|none|none|
|»» hash|string(byte)|false|none|none|
|block|object|false|none|none|
|» header|object|false|none|Header defines the structure of a Tendermint block header.|
|»» version|object|false|none|Consensus captures the consensus rules for processing a block in the blockchain,including all blockchain data structures and the rules of the application'sstate transition machine.|
|»»» block|string(uint64)|false|none|none|
|»»» app|string(uint64)|false|none|none|
|»» chain_id|string|false|none|none|
|»» height|string(int64)|false|none|none|
|»» time|string(date-time)|false|none|none|
|»» last_block_id|object|false|none|none|
|»»» hash|string(byte)|false|none|none|
|»»» part_set_header|object|false|none|none|
|»»»» total|integer(int64)|false|none|none|
|»»»» hash|string(byte)|false|none|none|
|»» last_commit_hash|string(byte)|false|none|commit from validators from the last block|
|»» data_hash|string(byte)|false|none|none|
|»» validators_hash|string(byte)|false|none|validators for the current block|
|»» next_validators_hash|string(byte)|false|none|none|
|»» consensus_hash|string(byte)|false|none|none|
|»» app_hash|string(byte)|false|none|none|
|»» last_results_hash|string(byte)|false|none|none|
|»» evidence_hash|string(byte)|false|none|evidence included in the block|
|»» proposer_address|string(byte)|false|none|none|
|» data|object|false|none|none|
|»» txs|[string]|false|none|Txs that will be applied by state @ block.Height+1.NOTE: not all txs here are valid.  We're just agreeing on the order first.This means that block.AppHash does not include these txs.|
|» evidence|object|false|none|none|
|»» evidence|[object]|false|none|none|
|»»» duplicate_vote_evidence|object|false|none|DuplicateVoteEvidence contains evidence of a validator signed two conflicting votes.|
|»»»» vote_a|object|false|none|Vote represents a prevote, precommit, or commit vote from validators forconsensus.|
|»»»»» type|string|false|none|SignedMsgType is a type of signed message in the consensus. - SIGNED_MSG_TYPE_PREVOTE: Votes - SIGNED_MSG_TYPE_PROPOSAL: Proposals|
|»»»»» height|string(int64)|false|none|none|
|»»»»» round|integer(int32)|false|none|none|
|»»»»» block_id|object|false|none|zero if vote is nil.|
|»»»»»» hash|string(byte)|false|none|none|
|»»»»»» part_set_header|object|false|none|none|
|»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»» hash|string(byte)|false|none|none|
|»»»»» timestamp|string(date-time)|false|none|none|
|»»»»» validator_address|string(byte)|false|none|none|
|»»»»» validator_index|integer(int32)|false|none|none|
|»»»»» signature|string(byte)|false|none|none|
|»»»» vote_b|object|false|none|Vote represents a prevote, precommit, or commit vote from validators forconsensus.|
|»»»»» type|string|false|none|SignedMsgType is a type of signed message in the consensus. - SIGNED_MSG_TYPE_PREVOTE: Votes - SIGNED_MSG_TYPE_PROPOSAL: Proposals|
|»»»»» height|string(int64)|false|none|none|
|»»»»» round|integer(int32)|false|none|none|
|»»»»» block_id|object|false|none|zero if vote is nil.|
|»»»»»» hash|string(byte)|false|none|none|
|»»»»»» part_set_header|object|false|none|none|
|»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»» hash|string(byte)|false|none|none|
|»»»»» timestamp|string(date-time)|false|none|none|
|»»»»» validator_address|string(byte)|false|none|none|
|»»»»» validator_index|integer(int32)|false|none|none|
|»»»»» signature|string(byte)|false|none|none|
|»»»» total_voting_power|string(int64)|false|none|none|
|»»»» validator_power|string(int64)|false|none|none|
|»»»» timestamp|string(date-time)|false|none|none|
|»»» light_client_attack_evidence|object|false|none|LightClientAttackEvidence contains evidence of a set of validators attempting to mislead a light client.|
|»»»» conflicting_block|object|false|none|none|
|»»»»» signed_header|object|false|none|none|
|»»»»»» header|object|false|none|Header defines the structure of a Tendermint block header.|
|»»»»»»» version|object|false|none|Consensus captures the consensus rules for processing a block in the blockchain,including all blockchain data structures and the rules of the application'sstate transition machine.|
|»»»»»»»» block|string(uint64)|false|none|none|
|»»»»»»»» app|string(uint64)|false|none|none|
|»»»»»»» chain_id|string|false|none|none|
|»»»»»»» height|string(int64)|false|none|none|
|»»»»»»» time|string(date-time)|false|none|none|
|»»»»»»» last_block_id|object|false|none|none|
|»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»» last_commit_hash|string(byte)|false|none|commit from validators from the last block|
|»»»»»»» data_hash|string(byte)|false|none|none|
|»»»»»»» validators_hash|string(byte)|false|none|validators for the current block|
|»»»»»»» next_validators_hash|string(byte)|false|none|none|
|»»»»»»» consensus_hash|string(byte)|false|none|none|
|»»»»»»» app_hash|string(byte)|false|none|none|
|»»»»»»» last_results_hash|string(byte)|false|none|none|
|»»»»»»» evidence_hash|string(byte)|false|none|evidence included in the block|
|»»»»»»» proposer_address|string(byte)|false|none|none|
|»»»»»» commit|object|false|none|Commit contains the evidence that a block was committed by a set of validators.|
|»»»»»»» height|string(int64)|false|none|none|
|»»»»»»» round|integer(int32)|false|none|none|
|»»»»»»» block_id|object|false|none|none|
|»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»» signatures|[object]|false|none|none|
|»»»»»»»» block_id_flag|string|false|none|none|
|»»»»»»»» validator_address|string(byte)|false|none|none|
|»»»»»»»» timestamp|string(date-time)|false|none|none|
|»»»»»»»» signature|string(byte)|false|none|none|
|»»»»» validator_set|object|false|none|none|
|»»»»»» validators|[object]|false|none|none|
|»»»»»»» address|string(byte)|false|none|none|
|»»»»»»» pub_key|object|false|none|none|
|»»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»»» proposer|object|false|none|none|
|»»»»»»» address|string(byte)|false|none|none|
|»»»»»»» pub_key|object|false|none|none|
|»»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»»» total_voting_power|string(int64)|false|none|none|
|»»»» common_height|string(int64)|false|none|none|
|»»»» byzantine_validators|[object]|false|none|none|
|»»»»» address|string(byte)|false|none|none|
|»»»»» pub_key|object|false|none|none|
|»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»» voting_power|string(int64)|false|none|none|
|»»»»» proposer_priority|string(int64)|false|none|none|
|»»»» total_voting_power|string(int64)|false|none|none|
|»»»» timestamp|string(date-time)|false|none|none|
|» last_commit|object|false|none|Commit contains the evidence that a block was committed by a set of validators.|
|»» height|string(int64)|false|none|none|
|»» round|integer(int32)|false|none|none|
|»» block_id|object|false|none|none|
|»»» hash|string(byte)|false|none|none|
|»»» part_set_header|object|false|none|none|
|»»»» total|integer(int64)|false|none|none|
|»»»» hash|string(byte)|false|none|none|
|»» signatures|[object]|false|none|none|
|»»» block_id_flag|string|false|none|none|
|»»» validator_address|string(byte)|false|none|none|
|»»» timestamp|string(date-time)|false|none|none|
|»»» signature|string(byte)|false|none|none|
|pagination|object|false|none|pagination defines a pagination for the response.|
|» next_key|string(byte)|false|none|none|
|» total|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|SIGNED_MSG_TYPE_UNKNOWN|
|type|SIGNED_MSG_TYPE_PREVOTE|
|type|SIGNED_MSG_TYPE_PRECOMMIT|
|type|SIGNED_MSG_TYPE_PROPOSAL|
|type|SIGNED_MSG_TYPE_UNKNOWN|
|type|SIGNED_MSG_TYPE_PREVOTE|
|type|SIGNED_MSG_TYPE_PRECOMMIT|
|type|SIGNED_MSG_TYPE_PROPOSAL|
|block_id_flag|BLOCK_ID_FLAG_UNKNOWN|
|block_id_flag|BLOCK_ID_FLAG_ABSENT|
|block_id_flag|BLOCK_ID_FLAG_COMMIT|
|block_id_flag|BLOCK_ID_FLAG_NIL|
|block_id_flag|BLOCK_ID_FLAG_UNKNOWN|
|block_id_flag|BLOCK_ID_FLAG_ABSENT|
|block_id_flag|BLOCK_ID_FLAG_COMMIT|
|block_id_flag|BLOCK_ID_FLAG_NIL|

## cosmos.tx.v1beta1.GetTxResponse

```json
{
  "tx": {
    "body": {
      "messages": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ],
      "memo": "string",
      "timeout_height": "string",
      "extension_options": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ],
      "non_critical_extension_options": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ]
    },
    "auth_info": {
      "signer_infos": [
        {
          "public_key": {
            "@type": "string",
            "property1": null,
            "property2": null
          },
          "mode_info": {
            "single": {
              "mode": "SIGN_MODE_UNSPECIFIED"
            },
            "multi": {
              "bitarray": {
                "extra_bits_stored": 0,
                "elems": "string"
              },
              "mode_infos": [
                {}
              ]
            }
          },
          "sequence": "string"
        }
      ],
      "fee": {
        "amount": [
          {
            "denom": "string",
            "amount": "string"
          }
        ],
        "gas_limit": "string",
        "payer": "string",
        "granter": "string"
      }
    },
    "signatures": [
      "string"
    ]
  },
  "tx_response": {
    "height": "string",
    "txhash": "string",
    "codespace": "string",
    "code": 0,
    "data": "string",
    "raw_log": "string",
    "logs": [
      {
        "msg_index": 0,
        "log": "string",
        "events": [
          {
            "type": "string",
            "attributes": [
              {
                "key": "string",
                "value": "string"
              }
            ]
          }
        ]
      }
    ],
    "info": "string",
    "gas_wanted": "string",
    "gas_used": "string",
    "tx": {
      "@type": "string",
      "property1": null,
      "property2": null
    },
    "timestamp": "string",
    "events": [
      {
        "type": "string",
        "attributes": [
          {
            "key": "string",
            "value": "string",
            "index": true
          }
        ]
      }
    ]
  }
}

```

GetTxResponse is the response type for the Service.GetTx method.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|[cosmos.tx.v1beta1.Tx](#schemacosmos.tx.v1beta1.tx)|false|none|Tx is the standard type used for broadcasting transactions.|
|tx_response|object|false|none|tx_response is the queried TxResponses.|
|» height|string(int64)|false|none|none|
|» txhash|string|false|none|The transaction hash.|
|» codespace|string|false|none|none|
|» code|integer(int64)|false|none|Response code.|
|» data|string|false|none|Result bytes, if any.|
|» raw_log|string|false|none|The output of the application's logger (raw string). May benon-deterministic.|
|» logs|[object]|false|none|The output of the application's logger (typed). May be non-deterministic.|
|»» msg_index|integer(int64)|false|none|none|
|»» log|string|false|none|none|
|»» events|[object]|false|none|Events contains a slice of Event objects that were emitted during someexecution.|
|»»» type|string|false|none|none|
|»»» attributes|[object]|false|none|none|
|»»»» key|string|false|none|none|
|»»»» value|string|false|none|none|
|» info|string|false|none|Additional information. May be non-deterministic.|
|» gas_wanted|string(int64)|false|none|Amount of gas requested for transaction.|
|» gas_used|string(int64)|false|none|Amount of gas consumed by transaction.|
|» tx|object|false|none|The request transaction bytes.|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» timestamp|string|false|none|Time of the previous block. For heights > 1, it's the weighted median ofthe timestamps of the valid votes in the block.LastCommit. For height == 1,it's genesis time.|
|» events|[object]|false|none|Events defines all the events emitted by processing a transaction. Note,these events include those emitted by processing all the messages and thoseemitted from the ante handler. Whereas Logs contains the events, withadditional metadata, emitted only by processing the messages.Since: cosmos-sdk 0.42.11, 0.44.5, 0.45|
|»» type|string|false|none|none|
|»» attributes|[object]|false|none|none|
|»»» key|string(byte)|false|none|none|
|»»» value|string(byte)|false|none|none|
|»»» index|boolean|false|none|none|

## cosmos.tx.v1beta1.GetTxsEventResponse

```json
{
  "txs": [
    {
      "body": {
        "messages": [
          {
            "@type": "string",
            "property1": null,
            "property2": null
          }
        ],
        "memo": "string",
        "timeout_height": "string",
        "extension_options": [
          {
            "@type": "string",
            "property1": null,
            "property2": null
          }
        ],
        "non_critical_extension_options": [
          {
            "@type": "string",
            "property1": null,
            "property2": null
          }
        ]
      },
      "auth_info": {
        "signer_infos": [
          {
            "public_key": {
              "@type": "string",
              "property1": null,
              "property2": null
            },
            "mode_info": {
              "single": {
                "mode": "SIGN_MODE_UNSPECIFIED"
              },
              "multi": {
                "bitarray": {
                  "extra_bits_stored": 0,
                  "elems": "string"
                },
                "mode_infos": [
                  {}
                ]
              }
            },
            "sequence": "string"
          }
        ],
        "fee": {
          "amount": [
            {
              "denom": "string",
              "amount": "string"
            }
          ],
          "gas_limit": "string",
          "payer": "string",
          "granter": "string"
        }
      },
      "signatures": [
        "string"
      ]
    }
  ],
  "tx_responses": [
    {
      "height": "string",
      "txhash": "string",
      "codespace": "string",
      "code": 0,
      "data": "string",
      "raw_log": "string",
      "logs": [
        {
          "msg_index": 0,
          "log": "string",
          "events": [
            {
              "type": "string",
              "attributes": [
                {
                  "key": "string",
                  "value": "string"
                }
              ]
            }
          ]
        }
      ],
      "info": "string",
      "gas_wanted": "string",
      "gas_used": "string",
      "tx": {
        "@type": "string",
        "property1": null,
        "property2": null
      },
      "timestamp": "string",
      "events": [
        {
          "type": "string",
          "attributes": [
            {
              "key": "string",
              "value": "string",
              "index": true
            }
          ]
        }
      ]
    }
  ],
  "pagination": {
    "next_key": "string",
    "total": "string"
  }
}

```

GetTxsEventResponse is the response type for the Service.TxsByEvents
RPC method.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|txs|[[cosmos.tx.v1beta1.Tx](#schemacosmos.tx.v1beta1.tx)]|false|none|txs is the list of queried transactions.|
|tx_responses|[object]|false|none|tx_responses is the list of queried TxResponses.|
|» height|string(int64)|false|none|none|
|» txhash|string|false|none|The transaction hash.|
|» codespace|string|false|none|none|
|» code|integer(int64)|false|none|Response code.|
|» data|string|false|none|Result bytes, if any.|
|» raw_log|string|false|none|The output of the application's logger (raw string). May benon-deterministic.|
|» logs|[object]|false|none|The output of the application's logger (typed). May be non-deterministic.|
|»» msg_index|integer(int64)|false|none|none|
|»» log|string|false|none|none|
|»» events|[object]|false|none|Events contains a slice of Event objects that were emitted during someexecution.|
|»»» type|string|false|none|none|
|»»» attributes|[object]|false|none|none|
|»»»» key|string|false|none|none|
|»»»» value|string|false|none|none|
|» info|string|false|none|Additional information. May be non-deterministic.|
|» gas_wanted|string(int64)|false|none|Amount of gas requested for transaction.|
|» gas_used|string(int64)|false|none|Amount of gas consumed by transaction.|
|» tx|object|false|none|The request transaction bytes.|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» timestamp|string|false|none|Time of the previous block. For heights > 1, it's the weighted median ofthe timestamps of the valid votes in the block.LastCommit. For height == 1,it's genesis time.|
|» events|[object]|false|none|Events defines all the events emitted by processing a transaction. Note,these events include those emitted by processing all the messages and thoseemitted from the ante handler. Whereas Logs contains the events, withadditional metadata, emitted only by processing the messages.Since: cosmos-sdk 0.42.11, 0.44.5, 0.45|
|»» type|string|false|none|none|
|»» attributes|[object]|false|none|none|
|»»» key|string(byte)|false|none|none|
|»»» value|string(byte)|false|none|none|
|»»» index|boolean|false|none|none|
|pagination|object|false|none|pagination defines a pagination for the response.|
|» next_key|string(byte)|false|none|none|
|» total|string(uint64)|false|none|none|

## cosmos.tx.v1beta1.ModeInfo

```json
{
  "single": {
    "mode": "SIGN_MODE_UNSPECIFIED"
  },
  "multi": {
    "bitarray": {
      "extra_bits_stored": 0,
      "elems": "string"
    },
    "mode_infos": [
      {
        "single": {
          "mode": "SIGN_MODE_UNSPECIFIED"
        },
        "multi": {}
      }
    ]
  }
}

```

ModeInfo describes the signing mode of a single or nested multisig signer.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|single|object|false|none|none|
|» mode|string|false|none|SignMode represents a signing mode with its own security guarantees. - SIGN_MODE_UNSPECIFIED: SIGN_MODE_UNSPECIFIED specifies an unknown signing mode and will berejected - SIGN_MODE_DIRECT: SIGN_MODE_DIRECT specifies a signing mode which uses SignDoc and isverified with raw bytes from Tx - SIGN_MODE_TEXTUAL: SIGN_MODE_TEXTUAL is a future signing mode that will verify somehuman-readable textual representation on top of the binary representationfrom SIGN_MODE_DIRECT - SIGN_MODE_LEGACY_AMINO_JSON: SIGN_MODE_LEGACY_AMINO_JSON is a backwards compatibility mode which usesAmino JSON and will be removed in the future - SIGN_MODE_EIP_191: SIGN_MODE_EIP_191 specifies the sign mode for EIP 191 signing on the CosmosSDK. Ref: https://eips.ethereum.org/EIPS/eip-191Currently, SIGN_MODE_EIP_191 is registered as a SignMode enum variant,but is not implemented on the SDK by default. To enable EIP-191, you needto pass a custom `TxConfig` that has an implementation of`SignModeHandler` for EIP-191. The SDK may decide to fully supportEIP-191 in the future.Since: cosmos-sdk 0.45.2|
|multi|[cosmos.tx.v1beta1.ModeInfo.Multi](#schemacosmos.tx.v1beta1.modeinfo.multi)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|mode|SIGN_MODE_UNSPECIFIED|
|mode|SIGN_MODE_DIRECT|
|mode|SIGN_MODE_TEXTUAL|
|mode|SIGN_MODE_LEGACY_AMINO_JSON|
|mode|SIGN_MODE_EIP_191|

## cosmos.tx.v1beta1.ModeInfo.Multi

```json
{
  "bitarray": {
    "extra_bits_stored": 0,
    "elems": "string"
  },
  "mode_infos": [
    {
      "single": {
        "mode": "SIGN_MODE_UNSPECIFIED"
      },
      "multi": {
        "bitarray": {
          "extra_bits_stored": 0,
          "elems": "string"
        },
        "mode_infos": []
      }
    }
  ]
}

```

Multi is the mode info for a multisig public key

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bitarray|object|false|none|CompactBitArray is an implementation of a space efficient bit array.This is used to ensure that the encoded data takes up a minimal amount ofspace after proto encoding.This is not thread safe, and is not intended for concurrent usage.|
|» extra_bits_stored|integer(int64)|false|none|none|
|» elems|string(byte)|false|none|none|
|mode_infos|[[cosmos.tx.v1beta1.ModeInfo](#schemacosmos.tx.v1beta1.modeinfo)]|false|none|[ModeInfo describes the signing mode of a single or nested multisig signer.]|

## cosmos.tx.v1beta1.SignerInfo

```json
{
  "public_key": {
    "@type": "string",
    "property1": null,
    "property2": null
  },
  "mode_info": {
    "single": {
      "mode": "SIGN_MODE_UNSPECIFIED"
    },
    "multi": {
      "bitarray": {
        "extra_bits_stored": 0,
        "elems": "string"
      },
      "mode_infos": [
        {}
      ]
    }
  },
  "sequence": "string"
}

```

SignerInfo describes the public key and signing mode of a single top-level
signer.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|public_key|object|false|none|public_key is the public key of the signer. It is optional for accountsthat already exist in state. If unset, the verifier can use the required \signer address for this position and lookup the public key.|
|» **additionalProperties**|any|false|none|none|
|» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|mode_info|[cosmos.tx.v1beta1.ModeInfo](#schemacosmos.tx.v1beta1.modeinfo)|false|none|ModeInfo describes the signing mode of a single or nested multisig signer.|
|sequence|string(uint64)|false|none|sequence is the sequence of the account, which describes thenumber of committed transactions signed by a given address. It is used toprevent replay attacks.|

## cosmos.tx.v1beta1.SimulateRequest

```json
{
  "tx": {
    "body": {
      "messages": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ],
      "memo": "string",
      "timeout_height": "string",
      "extension_options": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ],
      "non_critical_extension_options": [
        {
          "@type": "string",
          "property1": null,
          "property2": null
        }
      ]
    },
    "auth_info": {
      "signer_infos": [
        {
          "public_key": {
            "@type": "string",
            "property1": null,
            "property2": null
          },
          "mode_info": {
            "single": {
              "mode": "SIGN_MODE_UNSPECIFIED"
            },
            "multi": {
              "bitarray": {
                "extra_bits_stored": 0,
                "elems": "string"
              },
              "mode_infos": [
                {}
              ]
            }
          },
          "sequence": "string"
        }
      ],
      "fee": {
        "amount": [
          {
            "denom": "string",
            "amount": "string"
          }
        ],
        "gas_limit": "string",
        "payer": "string",
        "granter": "string"
      }
    },
    "signatures": [
      "string"
    ]
  },
  "tx_bytes": "string"
}

```

SimulateRequest is the request type for the Service.Simulate
RPC method.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|[cosmos.tx.v1beta1.Tx](#schemacosmos.tx.v1beta1.tx)|false|none|Tx is the standard type used for broadcasting transactions.|
|tx_bytes|string(byte)|false|none|tx_bytes is the raw transaction.Since: cosmos-sdk 0.43|

## cosmos.tx.v1beta1.Tx

```json
{
  "body": {
    "messages": [
      {
        "@type": "string",
        "property1": null,
        "property2": null
      }
    ],
    "memo": "string",
    "timeout_height": "string",
    "extension_options": [
      {
        "@type": "string",
        "property1": null,
        "property2": null
      }
    ],
    "non_critical_extension_options": [
      {
        "@type": "string",
        "property1": null,
        "property2": null
      }
    ]
  },
  "auth_info": {
    "signer_infos": [
      {
        "public_key": {
          "@type": "string",
          "property1": null,
          "property2": null
        },
        "mode_info": {
          "single": {
            "mode": "SIGN_MODE_UNSPECIFIED"
          },
          "multi": {
            "bitarray": {
              "extra_bits_stored": 0,
              "elems": "string"
            },
            "mode_infos": [
              {}
            ]
          }
        },
        "sequence": "string"
      }
    ],
    "fee": {
      "amount": [
        {
          "denom": "string",
          "amount": "string"
        }
      ],
      "gas_limit": "string",
      "payer": "string",
      "granter": "string"
    }
  },
  "signatures": [
    "string"
  ]
}

```

Tx is the standard type used for broadcasting transactions.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|body|object|false|none|TxBody is the body of a transaction that all signers sign over.|
|» messages|[object]|false|none|messages is a list of messages to be executed. The required signers ofthose messages define the number and order of elements in AuthInfo'ssigner_infos and Tx's signatures. Each required signer address is added tothe list only the first time it occurs.By convention, the first required signer (usually from the first message)is referred to as the primary signer and pays the fee for the wholetransaction.|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» memo|string|false|none|memo is any arbitrary note/comment to be added to the transaction.WARNING: in clients, any publicly exposed text should not be called memo,but should be called `note` instead (see https://github.com/cosmos/cosmos-sdk/issues/9122).|
|» timeout_height|string(uint64)|false|none|none|
|» extension_options|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» non_critical_extension_options|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|auth_info|[cosmos.tx.v1beta1.AuthInfo](#schemacosmos.tx.v1beta1.authinfo)|false|none|AuthInfo describes the fee and signer modes that are used to sign atransaction.|
|signatures|[string]|false|none|signatures is a list of signatures that matches the length and order ofAuthInfo's signer_infos to allow connecting signature meta information likepublic key and signing mode by position.|
