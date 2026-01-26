<!-- Generator: Widdershins v4.0.1 -->

<h1 id="">HTTP API Console — twilight-fork v</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="-query">Query</h1>

## TwilightprojectNyksForksDelegateKeysAll

<a id="opIdTwilightprojectNyksForksDelegateKeysAll"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/twilight-project/nyks/forks/delegate_keys_all \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/forks/delegate_keys_all`

*Queries a list of DelegateKeysAll items.*

> Example responses

> 200 Response

<h3 id="twilightprojectnyksforksdelegatekeysall-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

<h3 id="twilightprojectnyksforksdelegatekeysall-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» addresses|[object]|false|none|none|
|»» validatorAddress|string|false|none|none|
|»» btcOracleAddress|string|false|none|none|
|»» btcPublicKey|string|false|none|none|
|»» zkOracleAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serialized<br>protocol buffer message. This string must contain at least<br>one "/" character. The last segment of the URL's path must represent<br>the fully qualified name of the type (as in<br>`path/google.protobuf.Duration`). The name should be in a canonical form<br>(e.g., leading "." is not accepted).<br><br>In practice, teams usually precompile into the binary all types that they<br>expect it to use in the context of Any. However, for URLs which use the<br>scheme `http`, `https`, or no scheme, one can optionally set up a type<br>server that maps type URLs to message definitions as follows:<br><br>* If no scheme is provided, `https` is assumed.<br>* An HTTP GET on the URL must yield a [google.protobuf.Type][]<br>  value in binary format, or produce an error.<br>* Applications are allowed to cache lookup results based on the<br>  URL, or have them precompiled into a binary to avoid any<br>  lookup. Therefore, binary compatibility needs to be preserved<br>  on changes to types. (Use versioned type names to manage<br>  breaking changes.)<br><br>Note: this functionality is not currently available in the official<br>protobuf release, and it is not used for type URLs beginning with<br>type.googleapis.com.<br><br>Schemes other than `http`, `https` (or the empty scheme) might be<br>used with implementation specific semantics.|

<aside class="success">
This operation does not require authentication
</aside>

## TwilightprojectNyksForksDelegateKeysByBtcOracleAddress

<a id="opIdTwilightprojectNyksForksDelegateKeysByBtcOracleAddress"></a>

> Code samples

```shell
curl --request GET \
  --url https://example.com/twilight-project/nyks/forks/delegate_keys_by_btc_oracle_address/string \
  --header 'Accept: */*'
```

`GET /twilight-project/nyks/forks/delegate_keys_by_btc_oracle_address/{btcOracleAddress}`

*Queries a list of DelegateKeysByBtcOracleAddress items.*

<h3 id="twilightprojectnyksforksdelegatekeysbybtcoracleaddress-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|btcOracleAddress|path|string|true|none|

> Example responses

> 200 Response

<h3 id="twilightprojectnyksforksdelegatekeysbybtcoracleaddress-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

<h3 id="twilightprojectnyksforksdelegatekeysbybtcoracleaddress-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» addresses|object|false|none|none|
|»» validatorAddress|string|false|none|none|
|»» btcOracleAddress|string|false|none|none|
|»» btcPublicKey|string|false|none|none|
|»» zkOracleAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serialized<br>protocol buffer message. This string must contain at least<br>one "/" character. The last segment of the URL's path must represent<br>the fully qualified name of the type (as in<br>`path/google.protobuf.Duration`). The name should be in a canonical form<br>(e.g., leading "." is not accepted).<br><br>In practice, teams usually precompile into the binary all types that they<br>expect it to use in the context of Any. However, for URLs which use the<br>scheme `http`, `https`, or no scheme, one can optionally set up a type<br>server that maps type URLs to message definitions as follows:<br><br>* If no scheme is provided, `https` is assumed.<br>* An HTTP GET on the URL must yield a [google.protobuf.Type][]<br>  value in binary format, or produce an error.<br>* Applications are allowed to cache lookup results based on the<br>  URL, or have them precompiled into a binary to avoid any<br>  lookup. Therefore, binary compatibility needs to be preserved<br>  on changes to types. (Use versioned type names to manage<br>  breaking changes.)<br><br>Note: this functionality is not currently available in the official<br>protobuf release, and it is not used for type URLs beginning with<br>type.googleapis.com.<br><br>Schemes other than `http`, `https` (or the empty scheme) might be<br>used with implementation specific semantics.|

<aside class="success">
This operation does not require authentication
</aside>

