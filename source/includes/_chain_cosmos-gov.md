## Cosmos Governance Module

## Params

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/params/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/params/string', {
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
  "voting_params": {
    "voting_period": "voting_period..."
  },
  "deposit_params": {
    "min_deposit": [
      {
        "denom": "denom...",
        "amount": "1000"
      }
    ],
    "max_deposit_period": "max_deposit_period..."
  },
  "tally_params": {
    "quorum": "quorum...",
    "threshold": "threshold...",
    "veto_threshold": "veto_threshold..."
  }
}
```


`GET /cosmos/gov/v1beta1/params/{params_type}`

*Params queries all parameters of the gov module.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|params_type|path|string|true|params_type defines which parameters to query for, can be one of "voting",|

#### Detailed descriptions

**params_type**: params_type defines which parameters to query for, can be one of "voting",
"tallying" or "deposit".

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
|» voting_params|object|false|none|voting_params defines the parameters related to voting.|
|»» voting_period|string|false|none|Length of the voting period.|
|» deposit_params|object|false|none|deposit_params defines the parameters related to deposit.|
|»» min_deposit|[object]|false|none|Minimum deposit for a proposal to enter voting period.|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|
|»» max_deposit_period|string|false|none|Maximum period for Atom holders to deposit on a proposal. Initial value: 2 months.|
|» tally_params|object|false|none|tally_params defines the parameters related to tally.|
|»» quorum|string(byte)|false|none|Minimum percentage of total stake needed to vote for a result to be considered valid.|
|»» threshold|string(byte)|false|none|Minimum proportion of Yes votes for proposal to pass. Default value: 0.5.|
|»» veto_threshold|string(byte)|false|none|Minimum value of Veto votes to Total votes ratio for proposal to be vetoed. Default value: 1/3.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Proposals

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/proposals \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/proposals', {

> The result from the above endpoint looks like this:

```json
{
  "proposals": [
    {
      "proposal_id": "1000000",
      "content": {
        "@type": "@type..."
      },
      "status": "status..."
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

`GET /cosmos/gov/v1beta1/proposals`

*Proposals queries all proposals based on given status.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|proposal_status|query|string|false|proposal_status defines the status of the proposals.|
|voter|query|string|false|voter defines the voter address for the proposals.|
|depositor|query|string|false|depositor defines the deposit addresses from the proposals.|
|pagination.key|query|string(byte)|false|key is a value returned in PageResponse.next_key to begin|
|pagination.offset|query|string(uint64)|false|offset is a numeric offset that can be used when key is unavailable.|
|pagination.limit|query|string(uint64)|false|limit is the total number of results to be returned in the result page.|
|pagination.count_total|query|boolean|false|count_total is set to true  to indicate that the result set should include|
|pagination.reverse|query|boolean|false|reverse is set to true if results are to be returned in the descending order.|

#### Detailed descriptions

**proposal_status**: proposal_status defines the status of the proposals.

 - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default propopsal status.
 - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit
period.
 - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting
period.
 - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has
passed.
 - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has
been rejected.
 - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has
failed.

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

#### Enumerated Values

|Parameter|Value|
|---|---|
|proposal_status|PROPOSAL_STATUS_UNSPECIFIED|
|proposal_status|PROPOSAL_STATUS_DEPOSIT_PERIOD|
|proposal_status|PROPOSAL_STATUS_VOTING_PERIOD|
|proposal_status|PROPOSAL_STATUS_PASSED|
|proposal_status|PROPOSAL_STATUS_REJECTED|
|proposal_status|PROPOSAL_STATUS_FAILED|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryProposalsResponse is the response type for the Query/Proposals RPC
method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» proposals|[object]|false|none|none|
|»» proposal_id|string(uint64)|false|none|none|
|»» content|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» status|string|false|none|ProposalStatus enumerates the valid statuses of a proposal. - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default propopsal status. - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the depositperiod. - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the votingperiod. - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that haspassed. - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that hasbeen rejected. - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that hasfailed.|
|»» final_tally_result|object|false|none|TallyResult defines a standard tally for a governance proposal.|
|»»» yes|string|false|none|none|
|»»» abstain|string|false|none|none|
|»»» no|string|false|none|none|
|»»» no_with_veto|string|false|none|none|
|»» submit_time|string(date-time)|false|none|none|
|»» deposit_end_time|string(date-time)|false|none|none|
|»» total_deposit|[object]|false|none|none|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|
|»» voting_start_time|string(date-time)|false|none|none|
|»» voting_end_time|string(date-time)|false|none|none|
|» pagination|object|false|none|pagination defines the pagination in the response.|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|PROPOSAL_STATUS_UNSPECIFIED|
|status|PROPOSAL_STATUS_DEPOSIT_PERIOD|
|status|PROPOSAL_STATUS_VOTING_PERIOD|
|status|PROPOSAL_STATUS_PASSED|
|status|PROPOSAL_STATUS_REJECTED|
|status|PROPOSAL_STATUS_FAILED|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Proposal

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "proposal": {
    "proposal_id": "1000000",
    "content": {
      "@type": "@type..."
    },
    "status": "status...",
    "final_tally_result": {
      "yes": "yes...",
      "abstain": "abstain...",
      "no": "no..."
    },
    "submit_time": "submit_time...",
    "deposit_end_time": "deposit_end_time...",
    "total_deposit": [
      {
        "denom": "denom...",
        "amount": "1000"
      }
    ],
    "voting_start_time": "voting_start_time...",
    "voting_end_time": "voting_end_time..."
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/gov/v1beta1/proposals/{proposal_id}`

*Proposal queries proposal details based on ProposalID.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|proposal_id|path|string(uint64)|true|proposal_id defines the unique id of the proposal.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryProposalResponse is the response type for the Query/Proposal RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» proposal|object|false|none|Proposal defines the core field members of a governance proposal.|
|»» proposal_id|string(uint64)|false|none|none|
|»» content|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» status|string|false|none|ProposalStatus enumerates the valid statuses of a proposal. - PROPOSAL_STATUS_UNSPECIFIED: PROPOSAL_STATUS_UNSPECIFIED defines the default propopsal status. - PROPOSAL_STATUS_DEPOSIT_PERIOD: PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the depositperiod. - PROPOSAL_STATUS_VOTING_PERIOD: PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the votingperiod. - PROPOSAL_STATUS_PASSED: PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that haspassed. - PROPOSAL_STATUS_REJECTED: PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that hasbeen rejected. - PROPOSAL_STATUS_FAILED: PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that hasfailed.|
|»» final_tally_result|object|false|none|TallyResult defines a standard tally for a governance proposal.|
|»»» yes|string|false|none|none|
|»»» abstain|string|false|none|none|
|»»» no|string|false|none|none|
|»»» no_with_veto|string|false|none|none|
|»» submit_time|string(date-time)|false|none|none|
|»» deposit_end_time|string(date-time)|false|none|none|
|»» total_deposit|[object]|false|none|none|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|
|»» voting_start_time|string(date-time)|false|none|none|
|»» voting_end_time|string(date-time)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|PROPOSAL_STATUS_UNSPECIFIED|
|status|PROPOSAL_STATUS_DEPOSIT_PERIOD|
|status|PROPOSAL_STATUS_VOTING_PERIOD|
|status|PROPOSAL_STATUS_PASSED|
|status|PROPOSAL_STATUS_REJECTED|
|status|PROPOSAL_STATUS_FAILED|

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
  "deposits": [
    {
      "proposal_id": "1000000",
      "depositor": "depositor...",
      "amount": [
        {
          "denom": "denom...",
          "amount": "1000"
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

> This operation does not require authentication

## Deposits

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/deposits \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/deposits', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/gov/v1beta1/proposals/{proposal_id}/deposits`

*Deposits queries all deposits of a single proposal.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|proposal_id|path|string(uint64)|true|proposal_id defines the unique id of the proposal.|
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

*QueryDepositsResponse is the response type for the Query/Deposits RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» deposits|[object]|false|none|none|
|»» proposal_id|string(uint64)|false|none|none|
|»» depositor|string|false|none|none|
|»» amount|[object]|false|none|none|
|»»» denom|string|false|none|none|
|»»» amount|string|false|none|none|
|» pagination|object|false|none|pagination defines the pagination in the response.|
|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "deposit": {
    "proposal_id": "1000000",
    "depositor": "depositor...",
    "amount": [
      {
        "denom": "denom...",
        "amount": "1000"
      }
    ]
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

## Deposit

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/deposits/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/deposits/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/gov/v1beta1/proposals/{proposal_id}/deposits/{depositor}`

*Deposit queries single deposit information based proposalID, depositAddr.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|proposal_id|path|string(uint64)|true|proposal_id defines the unique id of the proposal.|
|depositor|path|string|true|depositor defines the deposit addresses from the proposals.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryDepositResponse is the response type for the Query/Deposit RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» deposit|object|false|none|deposit defines the requested deposit.|
|»» proposal_id|string(uint64)|false|none|none|
|»» depositor|string|false|none|none|

> The result from the above endpoint looks like this:

```json
{
  "tally": {
    "yes": "yes...",
    "abstain": "abstain...",
    "no": "no...",
    "no_with_veto": "no_with_veto..."
  }
}
```

|»» amount|[object]|false|none|none|
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

## TallyResult

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/tally \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/tally', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/gov/v1beta1/proposals/{proposal_id}/tally`

*TallyResult queries the tally of a proposal vote.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|proposal_id|path|string(uint64)|true|proposal_id defines the unique id of the proposal.|

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
  "votes": [
    {
      "proposal_id": "1000000",
      "voter": "voter...",
      "option": "option..."
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```


*QueryTallyResultResponse is the response type for the Query/Tally RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tally|object|false|none|TallyResult defines a standard tally for a governance proposal.|
|»» yes|string|false|none|none|
|»» abstain|string|false|none|none|
|»» no|string|false|none|none|
|»» no_with_veto|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Votes

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/votes \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/votes', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/gov/v1beta1/proposals/{proposal_id}/votes`

*Votes queries votes of a given proposal.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|proposal_id|path|string(uint64)|true|proposal_id defines the unique id of the proposal.|
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

*QueryVotesResponse is the response type for the Query/Votes RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» votes|[object]|false|none|votes defined the queried votes.|
|»» proposal_id|string(uint64)|false|none|none|
|»» voter|string|false|none|none|
|»» option|string|false|none|Deprecated: Prefer to use `options` instead. This field is set in queriesif and only if `len(options) == 1` and that option has weight 1. In allother cases, this field will default to VOTE_OPTION_UNSPECIFIED.|
|»» options|[object]|false|none|none|
|»»» option|string|false|none|VoteOption enumerates the valid vote options for a given governance proposal. - VOTE_OPTION_UNSPECIFIED: VOTE_OPTION_UNSPECIFIED defines a no-op vote option. - VOTE_OPTION_YES: VOTE_OPTION_YES defines a yes vote option. - VOTE_OPTION_ABSTAIN: VOTE_OPTION_ABSTAIN defines an abstain vote option. - VOTE_OPTION_NO: VOTE_OPTION_NO defines a no vote option. - VOTE_OPTION_NO_WITH_VETO: VOTE_OPTION_NO_WITH_VETO defines a no with veto vote option.|
|»»» weight|string|false|none|none|
|» pagination|object|false|none|pagination defines the pagination in the response.|

> The result from the above endpoint looks like this:

```json
{
  "vote": {
    "proposal_id": "1000000",
    "voter": "voter...",
    "option": "option...",
    "options": [
      {
        "option": "option...",
        "weight": "weight..."
      }
    ]
  }
}
```

|»» next_key|string(byte)|false|none|none|
|»» total|string(uint64)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|option|VOTE_OPTION_UNSPECIFIED|
|option|VOTE_OPTION_YES|
|option|VOTE_OPTION_ABSTAIN|
|option|VOTE_OPTION_NO|
|option|VOTE_OPTION_NO_WITH_VETO|
|option|VOTE_OPTION_UNSPECIFIED|
|option|VOTE_OPTION_YES|
|option|VOTE_OPTION_ABSTAIN|
|option|VOTE_OPTION_NO|
|option|VOTE_OPTION_NO_WITH_VETO|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## Vote

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/votes/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/gov/v1beta1/proposals/string/votes/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/gov/v1beta1/proposals/{proposal_id}/votes/{voter}`

*Vote queries voted information based on proposalID, voterAddr.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|proposal_id|path|string(uint64)|true|proposal_id defines the unique id of the proposal.|
|voter|path|string|true|voter defines the oter address for the proposals.|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*QueryVoteResponse is the response type for the Query/Vote RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» vote|object|false|none|vote defined the queried vote.|
|»» proposal_id|string(uint64)|false|none|none|
|»» voter|string|false|none|none|
|»» option|string|false|none|Deprecated: Prefer to use `options` instead. This field is set in queriesif and only if `len(options) == 1` and that option has weight 1. In allother cases, this field will default to VOTE_OPTION_UNSPECIFIED.|
|»» options|[object]|false|none|none|
|»»» option|string|false|none|VoteOption enumerates the valid vote options for a given governance proposal. - VOTE_OPTION_UNSPECIFIED: VOTE_OPTION_UNSPECIFIED defines a no-op vote option. - VOTE_OPTION_YES: VOTE_OPTION_YES defines a yes vote option. - VOTE_OPTION_ABSTAIN: VOTE_OPTION_ABSTAIN defines an abstain vote option. - VOTE_OPTION_NO: VOTE_OPTION_NO defines a no vote option. - VOTE_OPTION_NO_WITH_VETO: VOTE_OPTION_NO_WITH_VETO defines a no with veto vote option.|
|»»» weight|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|option|VOTE_OPTION_UNSPECIFIED|
|option|VOTE_OPTION_YES|
|option|VOTE_OPTION_ABSTAIN|
|option|VOTE_OPTION_NO|
|option|VOTE_OPTION_NO_WITH_VETO|
|option|VOTE_OPTION_UNSPECIFIED|
|option|VOTE_OPTION_YES|
|option|VOTE_OPTION_ABSTAIN|
|option|VOTE_OPTION_NO|
|option|VOTE_OPTION_NO_WITH_VETO|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication
