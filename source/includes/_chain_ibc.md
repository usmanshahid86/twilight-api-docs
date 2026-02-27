# Twilight Chain API 

## IBC Module

## IbcApplicationsTransferV1DenomTraces

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/apps/transfer/v1/denom_traces \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/apps/transfer/v1/denom_traces', {
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
  "denom_traces": [
    {
      "path": "path...",
      "base_denom": "base_denom..."
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```


`GET /ibc/apps/transfer/v1/denom_traces`

*DenomTraces queries all denomination traces.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|

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

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryConnectionsResponse is the response type for the Query/DenomTraces RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» denom_traces|[object]|false|none|denom_traces returns all denominations trace information.|
|»» path|string|false|none|path defines the chain of port/channel identifiers used for tracing thesource of the fungible token.|
|»» base_denom|string|false|none|base denomination of the relayed fungible token.|
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

## IbcApplicationsTransferV1DenomTrace

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/apps/transfer/v1/denom_traces/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/apps/transfer/v1/denom_traces/string', {

> The result from the above endpoint looks like this:

```json
{
  "denom_trace": {
    "path": "path...",
    "base_denom": "base_denom..."
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

`GET /ibc/apps/transfer/v1/denom_traces/{hash}`

*DenomTrace queries a denomination trace information.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|hash|path|string|true|hash (in hex format) of the denomination trace information.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDenomTraceResponse is the response type for the Query/DenomTrace RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» denom_trace|object|false|none|denom_trace returns the requested denomination trace information.|
|»» path|string|false|none|path defines the chain of port/channel identifiers used for tracing thesource of the fungible token.|
|»» base_denom|string|false|none|base denomination of the relayed fungible token.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcApplicationsTransferV1Params

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "params": {
    "send_enabled": true,
    "receive_enabled": true
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/ibc/apps/transfer/v1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/apps/transfer/v1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/apps/transfer/v1/params`

*Params queries all parameters of the ibc-transfer module.*

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
|»» send_enabled|boolean|false|none|send_enabled enables or disables all cross-chain token transfers from thischain.|
|»» receive_enabled|boolean|false|none|receive_enabled enables or disables all cross-chain token transfers to thischain.|

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
  "channels": [
    {
      "state": "state...",
      "ordering": "ordering...",
      "counterparty": {
        "port_id": "0x1234567890abcdef...",
        "channel_id": "0x1234567890abcdef..."
      }
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  },
  "height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

> This operation does not require authentication

## IbcCoreChannelV1Channels

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels`

*Channels queries all the IBC channels of a chain.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|

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

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryChannelsResponse is the response type for the Query/Channels RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» channels|[object]|false|none|list of stored channels of the chain.|
|»» state|string|false|none|State defines if a channel is in one of the following states:CLOSED, INIT, TRYOPEN, OPEN or UNINITIALIZED. - STATE_UNINITIALIZED_UNSPECIFIED: Default State - STATE_INIT: A channel has just started the opening handshake. - STATE_TRYOPEN: A channel has acknowledged the handshake step on the counterparty chain. - STATE_OPEN: A channel has completed the handshake. Open channels areready to send and receive packets. - STATE_CLOSED: A channel has been closed and can no longer be used to send or receivepackets.|
|»» ordering|string|false|none|- ORDER_NONE_UNSPECIFIED: zero-value for channel ordering - ORDER_UNORDERED: packets can be delivered in any order, which may differ from the order inwhich they were sent. - ORDER_ORDERED: packets are delivered exactly in the order which they were sent|
|»» counterparty|object|false|none|none|
|»»» port_id|string|false|none|port on the counterparty chain which owns the other end of the channel.|
|»»» channel_id|string|false|none|none|
|»» connection_hops|[string]|false|none|none|
|»» version|string|false|none|none|
|»» port_id|string|false|none|none|
|»» channel_id|string|false|none|none|
|» pagination|object|false|none|PageResponse is to be embedded in gRPC response messages where thecorresponding request message has used PageRequest. message SomeResponse {         repeated Bar results = 1;         PageResponse page = 2; }|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|
|» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|state|STATE_UNINITIALIZED_UNSPECIFIED|
|state|STATE_INIT|
|state|STATE_TRYOPEN|
|state|STATE_OPEN|
|state|STATE_CLOSED|
|ordering|ORDER_NONE_UNSPECIFIED|
|ordering|ORDER_UNORDERED|
|ordering|ORDER_ORDERED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "channel": {
    "state": "state...",
    "ordering": "ordering...",
    "counterparty": {
      "port_id": "0x1234567890abcdef...",
      "channel_id": "0x1234567890abcdef..."
    }
  },
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
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

## IbcCoreChannelV1Channel

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}`

*Channel queries an IBC Channel.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryChannelResponse is the response type for the Query/Channel RPC method.
Besides the Channel end, it includes a proof and the height from which the
proof was retrieved.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» channel|object|false|none|Channel defines pipeline for exactly-once packet delivery between specificmodules on separate blockchains, which has at least one end capable ofsending packets and one end capable of receiving packets.|
|»» state|string|false|none|State defines if a channel is in one of the following states:CLOSED, INIT, TRYOPEN, OPEN or UNINITIALIZED. - STATE_UNINITIALIZED_UNSPECIFIED: Default State - STATE_INIT: A channel has just started the opening handshake. - STATE_TRYOPEN: A channel has acknowledged the handshake step on the counterparty chain. - STATE_OPEN: A channel has completed the handshake. Open channels areready to send and receive packets. - STATE_CLOSED: A channel has been closed and can no longer be used to send or receivepackets.|
|»» ordering|string|false|none|- ORDER_NONE_UNSPECIFIED: zero-value for channel ordering - ORDER_UNORDERED: packets can be delivered in any order, which may differ from the order inwhich they were sent. - ORDER_ORDERED: packets are delivered exactly in the order which they were sent|
|»» counterparty|object|false|none|none|
|»»» port_id|string|false|none|port on the counterparty chain which owns the other end of the channel.|
|»»» channel_id|string|false|none|none|
|»» connection_hops|[string]|false|none|none|
|»» version|string|false|none|none|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|state|STATE_UNINITIALIZED_UNSPECIFIED|
|state|STATE_INIT|
|state|STATE_TRYOPEN|
|state|STATE_OPEN|
|state|STATE_CLOSED|

> The result from the above endpoint looks like this:

```json
{
  "identified_client_state": {
    "client_id": "0x1234567890abcdef...",
    "client_state": {
      "@type": "@type..."
    }
  },
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|ordering|ORDER_NONE_UNSPECIFIED|
|ordering|ORDER_UNORDERED|
|ordering|ORDER_ORDERED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1ChannelClientState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/client_state \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/client_state', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/client_state`

*ChannelClientState queries for the client state for the channel associated
with the provided channel identifiers.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryChannelClientStateResponse is the Response type for the
Query/QueryChannelClientState RPC method*

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "consensus_state": {
    "@type": "@type..."
  },
  "client_id": "0x1234567890abcdef...",
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|---|---|---|---|---|
|» identified_client_state|object|false|none|IdentifiedClientState defines a client state with an additional clientidentifier field.|
|»» client_id|string|false|none|none|
|»» client_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1ChannelConsensusState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/consensus_state/revision/string/height/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/consensus_state/revision/string/height/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/consensus_state/revision/{revision_number}/height/{revision_height}`

*ChannelConsensusState queries for the consensus state for the channel
associated with the provided channel identifiers.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|revision_number|path|string(uint64)|true|revision number of the consensus state|
|revision_height|path|string(uint64)|true|revision height of the consensus state|

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
  "next_sequence_receive": "1000000",
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

### Response Schema

Status Code **200**

*QueryChannelClientStateResponse is the Response type for the
Query/QueryChannelClientState RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» consensus_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» client_id|string|false|none|none|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1NextSequenceReceive

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/next_sequence \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/next_sequence', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/next_sequence`

*NextSequenceReceive returns the next receive sequence for a given channel.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|

> Example responses

> The result from the above endpoint looks like this:

```json
{
  "acknowledgements": [
    {
      "port_id": "0x1234567890abcdef...",
      "channel_id": "0x1234567890abcdef...",
      "sequence": "1000000"
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  },
  "height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```


> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QuerySequenceResponse is the request type for the
Query/QueryNextSequenceReceiveResponse RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» next_sequence_receive|string(uint64)|false|none|none|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1PacketAcknowledgements

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_acknowledgements \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_acknowledgements', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acknowledgements`

*PacketAcknowledgements returns all the packet acknowledgements associated
with a channel.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|
|packet_commitment_sequences|query|array[string]|false|list of packet sequences|

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


> The result from the above endpoint looks like this:

```json
{
  "acknowledgement": "acknowledgement...",
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
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

*QueryPacketAcknowledgemetsResponse is the request type for the
Query/QueryPacketAcknowledgements RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» acknowledgements|[object]|false|none|none|
|»» port_id|string|false|none|channel port identifier.|
|»» channel_id|string|false|none|channel unique identifier.|
|»» sequence|string(uint64)|false|none|packet sequence.|
|»» data|string(byte)|false|none|embedded data that represents packet state.|
|» pagination|object|false|none|PageResponse is to be embedded in gRPC response messages where thecorresponding request message has used PageRequest. message SomeResponse {         repeated Bar results = 1;         PageResponse page = 2; }|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|
|» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1PacketAcknowledgement

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_acks/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_acks/string', {
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
  "commitments": [
    {
      "port_id": "0x1234567890abcdef...",
      "channel_id": "0x1234567890abcdef...",
      "sequence": "1000000"
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  },
  "height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_acks/{sequence}`

*PacketAcknowledgement queries a stored packet acknowledgement hash.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|sequence|path|string(uint64)|true|packet sequence|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryPacketAcknowledgementResponse defines the client query response for a
packet which also includes a proof and the height from which the
proof was retrieved*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» acknowledgement|string(byte)|false|none|none|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1PacketCommitments

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments`

*PacketCommitments returns all the packet commitments hashes associated
with a channel.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|

#### Detailed descriptions

**pagination.key**: key is a value returned in PageResponse.next_key to begin
querying the next page most efficiently. Only one of offset or key

> The result from the above endpoint looks like this:

```json
{
  "sequences": [
    "1000000"
  ],
  "height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

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

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryPacketCommitmentsResponse is the request type for the
Query/QueryPacketCommitments RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» commitments|[object]|false|none|none|
|»» port_id|string|false|none|channel port identifier.|
|»» channel_id|string|false|none|channel unique identifier.|
|»» sequence|string(uint64)|false|none|packet sequence.|
|»» data|string(byte)|false|none|embedded data that represents packet state.|
|» pagination|object|false|none|PageResponse is to be embedded in gRPC response messages where thecorresponding request message has used PageRequest. message SomeResponse {         repeated Bar results = 1;         PageResponse page = 2; }|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|
|» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1UnreceivedAcks

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "sequences": [
    "1000000"
  ],
  "height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments/string/unreceived_acks \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments/string/unreceived_acks', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_ack_sequences}/unreceived_acks`

*UnreceivedAcks returns all the unreceived IBC acknowledgements associated
with a channel and sequences.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|packet_ack_sequences|path|array[string]|true|list of acknowledgement sequences|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryUnreceivedAcksResponse is the response type for the
Query/UnreceivedAcks RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» sequences|[string]|false|none|none|
|» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

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
  "commitment": "commitment...",
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

> This operation does not require authentication

## IbcCoreChannelV1UnreceivedPackets

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments/string/unreceived_packets \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments/string/unreceived_packets', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{packet_commitment_sequences}/unreceived_packets`

*UnreceivedPackets returns all the unreceived IBC packets associated with a
channel and sequences.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|packet_commitment_sequences|path|array[string]|true|list of packet sequences|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryUnreceivedPacketsResponse is the response type for the
Query/UnreceivedPacketCommitments RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» sequences|[string]|false|none|none|
|» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

> The result from the above endpoint looks like this:

```json
{
  "received": true,
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1PacketCommitment

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_commitments/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_commitments/{sequence}`

*PacketCommitment queries a stored packet commitment hash.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|sequence|path|string(uint64)|true|packet sequence|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryPacketCommitmentResponse defines the client query response for a packet
which also includes a proof and the height from which the proof was
retrieved*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» commitment|string(byte)|false|none|none|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|

> The result from the above endpoint looks like this:

```json
{
  "channels": [
    {
      "state": "state...",
      "ordering": "ordering...",
      "counterparty": {
        "port_id": "0x1234567890abcdef...",
        "channel_id": "0x1234567890abcdef..."
      }
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  },
  "height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1PacketReceipt

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_receipts/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/channels/string/ports/string/packet_receipts/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/channels/{channel_id}/ports/{port_id}/packet_receipts/{sequence}`

*PacketReceipt queries if a given packet sequence has been received on the
queried chain*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|channel_id|path|string|true|channel unique identifier|
|port_id|path|string|true|port unique identifier|
|sequence|path|string(uint64)|true|packet sequence|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryPacketReceiptResponse defines the client query response for a packet
receipt which also includes a proof, and the height from which the proof was
retrieved*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» received|boolean|false|none|none|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreChannelV1ConnectionChannels

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/channel/v1/connections/string/channels \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/channel/v1/connections/string/channels', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/channel/v1/connections/{connection}/channels`


> The result from the above endpoint looks like this:

```json
{
  "params": {
    "allowed_clients": [
      "item..."
    ]
  }
}
```

*ConnectionChannels queries all the channels associated with a connection
end.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|connection|path|string|true|connection unique identifier|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|

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

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryConnectionChannelsResponse is the Response type for the
Query/QueryConnectionChannels RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» channels|[object]|false|none|list of channels associated with a connection.|

> The result from the above endpoint looks like this:

```json
{
  "client_states": [
    {
      "client_id": "0x1234567890abcdef...",
      "client_state": {
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

|»» state|string|false|none|State defines if a channel is in one of the following states:CLOSED, INIT, TRYOPEN, OPEN or UNINITIALIZED. - STATE_UNINITIALIZED_UNSPECIFIED: Default State - STATE_INIT: A channel has just started the opening handshake. - STATE_TRYOPEN: A channel has acknowledged the handshake step on the counterparty chain. - STATE_OPEN: A channel has completed the handshake. Open channels areready to send and receive packets. - STATE_CLOSED: A channel has been closed and can no longer be used to send or receivepackets.|
|»» ordering|string|false|none|- ORDER_NONE_UNSPECIFIED: zero-value for channel ordering - ORDER_UNORDERED: packets can be delivered in any order, which may differ from the order inwhich they were sent. - ORDER_ORDERED: packets are delivered exactly in the order which they were sent|
|»» counterparty|object|false|none|none|
|»»» port_id|string|false|none|port on the counterparty chain which owns the other end of the channel.|
|»»» channel_id|string|false|none|none|
|»» connection_hops|[string]|false|none|none|
|»» version|string|false|none|none|
|»» port_id|string|false|none|none|
|»» channel_id|string|false|none|none|
|» pagination|object|false|none|PageResponse is to be embedded in gRPC response messages where thecorresponding request message has used PageRequest. message SomeResponse {         repeated Bar results = 1;         PageResponse page = 2; }|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|
|» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|state|STATE_UNINITIALIZED_UNSPECIFIED|
|state|STATE_INIT|
|state|STATE_TRYOPEN|
|state|STATE_OPEN|
|state|STATE_CLOSED|
|ordering|ORDER_NONE_UNSPECIFIED|
|ordering|ORDER_UNORDERED|
|ordering|ORDER_ORDERED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreClientV1ClientParams

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/client/v1/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/client/v1/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/client/v1/params`

*ClientParams queries all parameters of the ibc client.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryClientParamsResponse is the response type for the Query/ClientParams RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|

> The result from the above endpoint looks like this:

```json
{
  "client_state": {
    "@type": "@type..."
  },
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|» params|object|false|none|params defines the parameters of the module.|
|»» allowed_clients|[string]|false|none|allowed_clients defines the list of allowed client state types.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreClientV1ClientStates

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/client/v1/client_states \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/client/v1/client_states', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/client/v1/client_states`

*ClientStates queries all the IBC light clients of a chain.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|

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

> The result from the above endpoint looks like this:

```json
{
  "status": "status..."
}
```

is set.

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryClientStatesResponse is the response type for the Query/ClientStates RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» client_states|[object]|false|none|list of stored ClientStates of the chain.|
|»» client_id|string|false|none|none|
|»» client_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
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
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreClientV1ClientState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/client/v1/client_states/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/client/v1/client_states/string', {
  headers: {
    'Accept': '*/*'

> The result from the above endpoint looks like this:

```json
{
  "consensus_states": [
    {
      "height": {
        "revision_number": "1000000",
        "revision_height": "1000000"
      },
      "consensus_state": {
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

  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/client/v1/client_states/{client_id}`

*ClientState queries an IBC light client.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|client_id|path|string|true|client state unique identifier|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryClientStateResponse is the response type for the Query/ClientState RPC
method. Besides the client state, it includes a proof and the height from
which the proof was retrieved.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» client_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreClientV1ClientStatus

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/client/v1/client_status/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/client/v1/client_status/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/client/v1/client_status/{client_id}`

*Status queries the status of an IBC client.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|client_id|path|string|true|client unique identifier|

> Example responses


> The result from the above endpoint looks like this:

```json
{
  "consensus_state": {
    "@type": "@type..."
  },
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryClientStatusResponse is the response type for the Query/ClientStatus RPC
method. It returns the current status of the IBC client.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» status|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreClientV1ConsensusStates

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/client/v1/consensus_states/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/client/v1/consensus_states/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/client/v1/consensus_states/{client_id}`

*ConsensusStates queries all the consensus state associated with a given
client.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|client_id|path|string|true|client identifier|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|

#### Detailed descriptions

**pagination.key**: key is a value returned in PageResponse.next_key to begin
querying the next page most efficiently. Only one of offset or key
should be set.

> The result from the above endpoint looks like this:

```json
{
  "upgraded_client_state": {
    "@type": "@type..."
  }
}
```


**pagination.offset**: offset is a numeric offset that can be used when key is unavailable.
It is less efficient than using key. Only one of offset or key should
be set.

**pagination.limit**: limit is the total number of results to be returned in the result page.
If left empty it will default to a value to be set by each app.

**pagination.count_total**: count_total is set to true  to indicate that the result set should include
a count of the total number of items available for pagination in UIs.
count_total is only respected when offset is used. It is ignored when key
is set.

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryConsensusStatesResponse is the response type for the
Query/ConsensusStates RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» consensus_states|[object]|false|none|none|
|»» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»»» revision_number|string(uint64)|false|none|none|
|»»» revision_height|string(uint64)|false|none|none|
|»» consensus_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
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
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> The result from the above endpoint looks like this:

```json
{
  "upgraded_consensus_state": {
    "@type": "@type..."
  }
}
```


> This operation does not require authentication

## IbcCoreClientV1ConsensusState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/client/v1/consensus_states/string/revision/string/height/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/client/v1/consensus_states/string/revision/string/height/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/client/v1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}`

*ConsensusState queries a consensus state associated with a client state at
a given height.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|client_id|path|string|true|client identifier|
|revision_number|path|string(uint64)|true|consensus state revision number|
|revision_height|path|string(uint64)|true|consensus state revision height|
|latest_height|query|boolean|false|latest_height overrrides the height field and queries the latest stored|

#### Detailed descriptions

**latest_height**: latest_height overrrides the height field and queries the latest stored
ConsensusState

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
  "connection_paths": [
    "item..."
  ],
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

### Response Schema

Status Code **200**

*QueryConsensusStateResponse is the response type for the Query/ConsensusState
RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» consensus_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreClientV1UpgradedClientState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/client/v1/upgraded_client_states \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/client/v1/upgraded_client_states', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/client/v1/upgraded_client_states`

*UpgradedClientState queries an Upgraded IBC light client.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|

> The result from the above endpoint looks like this:

```json
{
  "connections": [
    {
      "id": "0x1234567890abcdef...",
      "client_id": "0x1234567890abcdef...",
      "versions": [
        {
          "identifier": "0x1234567890abcdef...",
          "features": [
            "item..."
          ]
        }
      ]
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  },
  "height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryUpgradedClientStateResponse is the response type for the
Query/UpgradedClientState RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» upgraded_client_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
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

## IbcCoreClientV1UpgradedConsensusState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/client/v1/upgraded_consensus_states \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/client/v1/upgraded_consensus_states', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/client/v1/upgraded_consensus_states`

*UpgradedConsensusState queries an Upgraded IBC consensus state.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryUpgradedConsensusStateResponse is the response type for the
Query/UpgradedConsensusState RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» upgraded_consensus_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
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

## IbcCoreConnectionV1ClientConnections

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/connection/v1/client_connections/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/connection/v1/client_connections/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);

> The result from the above endpoint looks like this:

```json
{
  "connection": {
    "client_id": "0x1234567890abcdef...",
    "versions": [
      {
        "identifier": "0x1234567890abcdef...",
        "features": [
          "item..."
        ]
      }
    ],
    "state": "state..."
  },
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

```

`GET /ibc/core/connection/v1/client_connections/{client_id}`

*ClientConnections queries the connection paths associated with a client
state.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|client_id|path|string|true|client identifier associated with a connection|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryClientConnectionsResponse is the response type for the
Query/ClientConnections RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» connection_paths|[string]|false|none|slice of all the connection paths associated with a client.|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreConnectionV1Connections

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/connection/v1/connections \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/connection/v1/connections', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/connection/v1/connections`

*Connections queries all the IBC connections of a chain.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|

> The result from the above endpoint looks like this:

```json
{
  "identified_client_state": {
    "client_id": "0x1234567890abcdef...",
    "client_state": {
      "@type": "@type..."
    }
  },
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|

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

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryConnectionsResponse is the response type for the Query/Connections RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» connections|[object]|false|none|list of stored connections of the chain.|
|»» id|string|false|none|connection identifier.|
|»» client_id|string|false|none|client associated with this connection.|
|»» versions|[object]|false|none|none|
|»»» identifier|string|false|none|none|
|»»» features|[string]|false|none|none|
|»» state|string|false|none|current state of the connection end.|
|»» counterparty|object|false|none|counterparty chain associated with this connection.|
|»»» client_id|string|false|none|identifies the client on the counterparty chain associated with a givenconnection.|
|»»» connection_id|string|false|none|identifies the connection end on the counterparty chain associated with agiven connection.|
|»»» prefix|object|false|none|commitment merkle prefix of the counterparty chain.|
|»»»» key_prefix|string(byte)|false|none|none|
|»» delay_period|string(uint64)|false|none|delay period associated with this connection.|
|» pagination|object|false|none|PageResponse is to be embedded in gRPC response messages where thecorresponding request message has used PageRequest. message SomeResponse {         repeated Bar results = 1;         PageResponse page = 2; }|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|
|» height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|state|STATE_UNINITIALIZED_UNSPECIFIED|
|state|STATE_INIT|

> The result from the above endpoint looks like this:

```json
{
  "consensus_state": {
    "@type": "@type..."
  },
  "client_id": "0x1234567890abcdef...",
  "proof": "proof...",
  "proof_height": {
    "revision_number": "1000000",
    "revision_height": "1000000"
  }
}
```

|state|STATE_TRYOPEN|
|state|STATE_OPEN|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreConnectionV1Connection

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/connection/v1/connections/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/connection/v1/connections/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/connection/v1/connections/{connection_id}`

*Connection queries an IBC connection end.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|connection_id|path|string|true|connection unique identifier|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryConnectionResponse is the response type for the Query/Connection RPC
method. Besides the connection end, it includes a proof and the height from
which the proof was retrieved.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» connection|object|false|none|ConnectionEnd defines a stateful object on a chain connected to anotherseparate one.NOTE: there must only be 2 defined ConnectionEnds to establisha connection between two chains.|
|»» client_id|string|false|none|client associated with this connection.|
|»» versions|[object]|false|none|IBC version which can be utilised to determine encodings or protocols forchannels or packets utilising this connection.|
|»»» identifier|string|false|none|none|
|»»» features|[string]|false|none|none|
|»» state|string|false|none|current state of the connection end.|
|»» counterparty|object|false|none|counterparty chain associated with this connection.|
|»»» client_id|string|false|none|identifies the client on the counterparty chain associated with a givenconnection.|
|»»» connection_id|string|false|none|identifies the connection end on the counterparty chain associated with agiven connection.|
|»»» prefix|object|false|none|commitment merkle prefix of the counterparty chain.|
|»»»» key_prefix|string(byte)|false|none|none|
|»» delay_period|string(uint64)|false|none|delay period that must pass before a consensus state can be used forpacket-verification NOTE: delay period logic is only implemented by someclients.|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|state|STATE_UNINITIALIZED_UNSPECIFIED|
|state|STATE_INIT|
|state|STATE_TRYOPEN|
|state|STATE_OPEN|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreConnectionV1ConnectionClientState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/connection/v1/connections/string/client_state \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/connection/v1/connections/string/client_state', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/connection/v1/connections/{connection_id}/client_state`

*ConnectionClientState queries the client state associated with the
connection.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|connection_id|path|string|true|connection identifier|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryConnectionClientStateResponse is the response type for the
Query/ConnectionClientState RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» identified_client_state|object|false|none|IdentifiedClientState defines a client state with an additional clientidentifier field.|
|»» client_id|string|false|none|none|
|»» client_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## IbcCoreConnectionV1ConnectionConsensusState

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/ibc/core/connection/v1/connections/string/consensus_state/revision/string/height/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/ibc/core/connection/v1/connections/string/consensus_state/revision/string/height/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /ibc/core/connection/v1/connections/{connection_id}/consensus_state/revision/{revision_number}/height/{revision_height}`

*ConnectionConsensusState queries the consensus state associated with the
connection.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|connection_id|path|string|true|connection identifier|
|revision_number|path|string(uint64)|true|none|
|revision_height|path|string(uint64)|true|none|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryConnectionConsensusStateResponse is the response type for the
Query/ConnectionConsensusState RPC method*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» consensus_state|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|» client_id|string|false|none|none|
|» proof|string(byte)|false|none|none|
|» proof_height|object|false|none|Normally the RevisionHeight is incremented at each height while keepingRevisionNumber the same. However some consensus algorithms may choose toreset the height in certain conditions e.g. hard forks, state-machinebreaking changes In these cases, the RevisionNumber is incremented so thatheight continues to be monitonically increasing even as the RevisionHeightgets reset|
|»» revision_number|string(uint64)|false|none|none|
|»» revision_height|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication
