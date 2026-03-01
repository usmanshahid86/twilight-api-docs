## Twilight Volt Module

## BtcReserve

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/btc_reserve \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/btc_reserve', {
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
  "BtcReserves": [
    {
      "ReserveId": "1000000",
      "ReserveAddress": "0x1234567890abcdef...",
      "JudgeAddress": "0x1234567890abcdef...",
      "BtcRelayCapacityValue": "1000000",
      "TotalValue": "1000000",
      "PrivatePoolValue": "1000000",
      "PublicValue": "1000000",
      "FeePool": "1000000",
      "UnlockHeight": "1000000",
      "RoundId": "1000000"
    }
  ]
}
```


`GET /twilight-project/nyks/volt/btc_reserve`

*Queries a list of BtcReserve items.*

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
|» BtcReserves|[object]|false|none|none|
|»» BtcReserve is a mapping of a validator address to a reserve ID
It holds other values in the reserve struct such as total
value, private pool value, public pool value, and the btc relay capacity value|object|false|none|none|
|»»» ReserveId|string(uint64)|false|none|none|
|»»» ReserveAddress|string|false|none|none|
|»»» JudgeAddress|string|false|none|none|
|»»» BtcRelayCapacityValue|string(uint64)|false|none|none|
|»»» TotalValue|string(uint64)|false|none|none|
|»»» PrivatePoolValue|string(uint64)|false|none|none|
|»»» PublicValue|string(uint64)|false|none|none|
|»»» FeePool|string(uint64)|false|none|none|
|»»» UnlockHeight|string(uint64)|false|none|none|
|»»» RoundId|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## BtcWithdrawRequest

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/btc_withdraw_request/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/btc_withdraw_request/string', {

> The result from the above endpoint looks like this:

```json
{
  "BtcWithdrawRequest": {
    "withdrawIdentifier": 0,
    "withdrawAddress": "0x1234567890abcdef...",
    "withdrawReserveId": "1000000",
    "withdrawAmount": "1000000",
    "twilightAddress": "twilight1abc123def456...",
    "isConfirmed": true,
    "CreationTwilightBlockHeight": "CreationTwilightBlockHeight..."
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

`GET /twilight-project/nyks/volt/btc_withdraw_request/{twilightAddress}`

*Queries a list of BtcWithdrawRequest items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|twilightAddress|path|string|true|none|
|reserveId|query|string(uint64)|false|none|
|btcAddress|query|string|false|none|
|withdrawAmount|query|string(uint64)|false|none|

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
|» BtcWithdrawRequest|object|false|none|none|
|»» withdrawIdentifier|integer(int64)|false|none|none|
|»» withdrawAddress|string|false|none|none|
|»» withdrawReserveId|string(uint64)|false|none|none|
|»» withdrawAmount|string(uint64)|false|none|none|
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

## ClearingAccount

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "ClearingAccount": {
    "TwilightAddress": "twilight1abc123def456...",
    "BtcDepositAddress": "0x1234567890abcdef...",
    "BtcDepositAddressIdentifier": 0,
    "BtcWithdrawAddress": "0x1234567890abcdef...",
    "BtcWithdrawAddressIdentifier": 0,
    "ReserveAccountBalances": [
      {
        "ReserveId": "1000000",
        "Amount": "1000000"
      }
    ]
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/clearing_account/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/clearing_account/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/clearing_account/{twilightAddress}`

*Queries a list of ClearingAccount items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|twilightAddress|path|string|true|none|

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
|» ClearingAccount|object|false|none|none|
|»» TwilightAddress|string|false|none|none|
|»» BtcDepositAddress|string|false|none|none|
|»» BtcDepositAddressIdentifier|integer(int64)|false|none|none|
|»» BtcWithdrawAddress|string|false|none|none|
|»» BtcWithdrawAddressIdentifier|integer(int64)|false|none|none|
|»» ReserveAccountBalances|[object]|false|none|none|
|»»» ReserveId|string(uint64)|false|none|none|
|»»» Amount|string(uint64)|false|none|none|

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
  "Fragment": {
    "FragmentId": "1000000",
    "FragmentStatus": true,
    "JudgeAddress": "0x1234567890abcdef...",
    "JudgeStatus": true,
    "Signers": [
      {
        "FragmentID": "1000000",
        "SignerAddress": "0x1234567890abcdef...",
        "SignerStatus": true
      }
    ],
    "SignerApplicationFee": "1000000",
    "Threshold": "1000000",
    "FeePool": "1000000",
    "FragmentFeeBips": "1000000",
    "arbitraryData": "arbitraryData...",
    "ReserveIds": [
      "1000000"
    ]
  }
}
```

> This operation does not require authentication

## FragmentById

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/fragment_by_id/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/fragment_by_id/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/fragment_by_id/{fragmentId}`

*Queries a list of FragmentById items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|fragmentId|path|string(uint64)|true|none|

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
|» Fragment|object|false|none|none|
|»» FragmentId|string(uint64)|false|none|none|
|»» FragmentStatus|boolean|false|none|none|
|»» JudgeAddress|string|false|none|none|
|»» JudgeStatus|boolean|false|none|none|
|»» Signers|[object]|false|none|none|
|»»» FragmentID|string(uint64)|false|none|none|
|»»» SignerAddress|string|false|none|none|
|»»» SignerStatus|boolean|false|none|none|
|»»» SignerBtcPublicKey|string|false|none|none|
|»»» SignerApplicationFee|string(uint64)|false|none|none|
|»»» SignerFeeBips|string(uint64)|false|none|none|
|»» SignerApplicationFee|string(uint64)|false|none|none|
|»» Threshold|string(uint64)|false|none|none|
|»» FeePool|string(uint64)|false|none|none|
|»» FragmentFeeBips|string(uint64)|false|none|none|
|»» arbitraryData|string|false|none|none|
|»» ReserveIds|[string]|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "Fragments": [
    {
      "FragmentId": "1000000",
      "FragmentStatus": true,
      "JudgeAddress": "0x1234567890abcdef...",
      "JudgeStatus": true,
      "Signers": [
        {
          "FragmentID": "1000000",
          "SignerAddress": "0x1234567890abcdef...",
          "SignerStatus": true
        }
      ],
      "SignerApplicationFee": "1000000",
      "Threshold": "1000000",
      "FeePool": "1000000",
      "FragmentFeeBips": "1000000",
      "arbitraryData": "arbitraryData...",
      "ReserveIds": [
        "1000000"
      ]
    }
  ]
}
```

|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## GetAllFragments

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/get_all_fragments \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/get_all_fragments', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/get_all_fragments`

*Queries a list of GetAllFragments items.*

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
|» Fragments|[object]|false|none|none|
|»» FragmentId|string(uint64)|false|none|none|
|»» FragmentStatus|boolean|false|none|none|
|»» JudgeAddress|string|false|none|none|
|»» JudgeStatus|boolean|false|none|none|
|»» Signers|[object]|false|none|none|
|»»» FragmentID|string(uint64)|false|none|none|
|»»» SignerAddress|string|false|none|none|
|»»» SignerStatus|boolean|false|none|none|
|»»» SignerBtcPublicKey|string|false|none|none|
|»»» SignerApplicationFee|string(uint64)|false|none|none|
|»»» SignerFeeBips|string(uint64)|false|none|none|
|»» SignerApplicationFee|string(uint64)|false|none|none|
|»» Threshold|string(uint64)|false|none|none|
|»» FeePool|string(uint64)|false|none|none|

> The result from the above endpoint looks like this:

```json
{
  "params": {}
}
```

|»» FragmentFeeBips|string(uint64)|false|none|none|
|»» arbitraryData|string|false|none|none|
|»» ReserveIds|[string]|false|none|none|

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
  --url https://lcd.twilight.org/twilight-project/nyks/volt/params \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/params', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/params`

*Parameters queries the parameters of the module.*

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
  "RefundTxSnapshot": {
    "ReserveId": "1000000",
    "RoundId": "1000000",
    "refundAccounts": [
      {
        "Amount": "1000000",
        "BtcDepositAddress": "0x1234567890abcdef...",
        "BtcDepositAddressIdentifier": 0
      }
    ],
    "EndBlockerHeightTwilight": "EndBlockerHeightTwilight..."
  }
}
```


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

## RefundTxSnapshot

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/refund_tx_snapshot/string/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/refund_tx_snapshot/string/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/refund_tx_snapshot/{reserveId}/{roundId}`

*Queries a list of RefundTxSnapshot items.*

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

> The result from the above endpoint looks like this:

```json
{
  "ReserveClearingAccountsAll": [
    {
      "TwilightAddress": "twilight1abc123def456...",
      "BtcDepositAddress": "0x1234567890abcdef...",
      "BtcDepositAddressIdentifier": 0,
      "BtcWithdrawAddress": "0x1234567890abcdef...",
      "BtcWithdrawAddressIdentifier": 0,
      "ReserveAccountBalances": [
        {
          "ReserveId": "1000000",
          "Amount": "1000000"
        }
      ]
    }
  ]
}
```

|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» RefundTxSnapshot|object|false|none|none|
|»» ReserveId|string(uint64)|false|none|none|
|»» RoundId|string(uint64)|false|none|none|
|»» refundAccounts|[object]|false|none|none|
|»»» RefundTxSnap is used to keep a mapping of the last refund transaction for a reserve|object|false|none|none|
|»»»» Amount|string(uint64)|false|none|none|
|»»»» BtcDepositAddress|string|false|none|none|
|»»»» BtcDepositAddressIdentifier|integer(int64)|false|none|none|
|»» EndBlockerHeightTwilight|string(int64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## ReserveClearingAccountsAll

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/reserve_clearing_accounts_all/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/reserve_clearing_accounts_all/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/reserve_clearing_accounts_all/{reserveId}`

*Queries a list of ReserveClearingAccountsAll items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|

> Example responses

> 200 Response

> The result from the above endpoint looks like this:

```json
{
  "ReserveWithdrawPool": {
    "ReserveID": "1000000",
    "RoundID": "1000000",
    "processingWithdrawIdentifiers": [
      0
    ],
    "queuedWithdrawIdentifiers": [
      0
    ],
    "currentProcessingIndex": 0
  }
}
```


### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» ReserveClearingAccountsAll|[object]|false|none|none|
|»» ClearingAccount is used to keep a mapping of how a user's addresses and its reserve account balances|object|false|none|none|
|»»» TwilightAddress|string|false|none|none|
|»»» BtcDepositAddress|string|false|none|none|
|»»» BtcDepositAddressIdentifier|integer(int64)|false|none|none|
|»»» BtcWithdrawAddress|string|false|none|none|
|»»» BtcWithdrawAddressIdentifier|integer(int64)|false|none|none|
|»»» ReserveAccountBalances|[object]|false|none|none|
|»»»» ReserveId|string(uint64)|false|none|none|
|»»»» Amount|string(uint64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## ReserveWithdrawPool

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/reserve_withdraw_pool/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/reserve_withdraw_pool/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/reserve_withdraw_pool/{reserveId}`


> The result from the above endpoint looks like this:

```json
{
  "ReserveWithdrawSnapshot": {
    "ReserveId": "1000000",
    "RoundId": "1000000",
    "withdrawRequests": [
      {
        "withdrawIdentifier": 0,
        "withdrawAddress": "0x1234567890abcdef...",
        "withdrawAmount": "1000000"
      }
    ],
    "EndBlockerHeightTwilight": "EndBlockerHeightTwilight..."
  }
}
```

*Queries a list of ReserveWithdrawPool items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|reserveId|path|string(uint64)|true|none|

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
|» ReserveWithdrawPool|object|false|none|none|
|»» ReserveID|string(uint64)|false|none|none|
|»» RoundID|string(uint64)|false|none|none|
|»» processingWithdrawIdentifiers|[integer]|false|none|none|
|»» queuedWithdrawIdentifiers|[integer]|false|none|none|
|»» currentProcessingIndex|integer(int64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## ReserveWithdrawSnapshot

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/reserve_withdraw_snapshot/string/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/reserve_withdraw_snapshot/string/string', {
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
  "SignerApplications": [
    {
      "applicationId": "1000000",
      "fragmentId": "1000000",
      "applicationFee": "1000000",
      "feeBips": "1000000",
      "btcPubKey": "btcPubKey...",
      "signerAddress": "0x1234567890abcdef..."
    }
  ]
}
```


`GET /twilight-project/nyks/volt/reserve_withdraw_snapshot/{reserveId}/{roundId}`

*Queries a list of ReserveWithdrawSnapshot items.*

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
|» ReserveWithdrawSnapshot|object|false|none|none|
|»» ReserveId|string(uint64)|false|none|none|
|»» RoundId|string(uint64)|false|none|none|
|»» withdrawRequests|[object]|false|none|none|
|»»» WithdrawRequestSnap is a snapshot of the withdraw request|object|false|none|none|
|»»»» withdrawIdentifier|integer(int64)|false|none|none|
|»»»» withdrawAddress|string|false|none|none|
|»»»» withdrawAmount|string(uint64)|false|none|none|
|»» EndBlockerHeightTwilight|string(int64)|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication

## SignerApplications

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/twilight-project/nyks/volt/signer_applications/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/twilight-project/nyks/volt/signer_applications/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /twilight-project/nyks/volt/signer_applications/{fragmentId}`

*Queries a list of SignerApplications items.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|fragmentId|path|string(uint64)|true|none|

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
|» SignerApplications|[object]|false|none|none|
|»» applicationId|string(uint64)|false|none|none|
|»» fragmentId|string(uint64)|false|none|none|
|»» applicationFee|string(uint64)|false|none|none|
|»» feeBips|string(uint64)|false|none|none|
|»» btcPubKey|string|false|none|none|
|»» signerAddress|string|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|none|

> This operation does not require authentication
