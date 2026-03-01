## Cosmos Tendermint Module

## CosmosBaseTendermintV1Beta1GetLatestBlock

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/blocks/latest \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/blocks/latest', {
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
  "block_id": {
    "hash": "0x1234567890abcdef...",
    "part_set_header": {
      "total": 0,
      "hash": "0x1234567890abcdef..."
    }
  },
  "block": {
    "header": {
      "version": {
        "block": "1000000",
        "app": "1000000"
      },
      "chain_id": "0x1234567890abcdef...",
      "height": "height..."
    },
    "data": {
      "txs": [
        "item..."
      ]
    },
    "evidence": {
      "evidence": [
        {
          "duplicate_vote_evidence": {
            "vote_a": {
              "type": "type...",
              "height": "height...",
              "round": 0
            },
            "vote_b": {
              "type": "type...",
              "height": "height...",
              "round": 0
            },
            "total_voting_power": "total_voting_power..."
          },
          "light_client_attack_evidence": {
            "conflicting_block": {
              "signed_header": {
                "header": {
                  "version": {
                    "block": "1000000",
                    "app": "1000000"
                  },
                  "chain_id": "0x1234567890abcdef...",
                  "height": "height..."
                },
                "commit": {
                  "height": "height...",
                  "round": 0,
                  "block_id": {
                    "hash": "0x1234567890abcdef...",
                    "part_set_header": {
                      "total": 0,
                      "hash": "0x1234567890abcdef..."
                    }
                  }
                }
              },
              "validator_set": {
                "validators": [
                  {
                    "address": "0x1234567890abcdef...",
                    "pub_key": {
                      "ed25519": "ed25519...",
                      "secp256k1": "secp256k1..."
                    },
                    "voting_power": "voting_power..."
                  }
                ],
                "proposer": {
                  "address": "0x1234567890abcdef...",
                  "pub_key": {
                    "ed25519": "ed25519...",
                    "secp256k1": "secp256k1..."
                  },
                  "voting_power": "voting_power..."
                },
                "total_voting_power": "total_voting_power..."
              }
            },
            "common_height": "common_height...",
            "byzantine_validators": [
              {
                "address": "0x1234567890abcdef...",
                "pub_key": {
                  "ed25519": "ed25519...",
                  "secp256k1": "secp256k1..."
                },
                "voting_power": "voting_power..."
              }
            ]
          }
        }
      ]
    }
  }
}
```


`GET /cosmos/base/tendermint/v1beta1/blocks/latest`

*GetLatestBlock returns the latest block.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*GetLatestBlockResponse is the response type for the Query/GetLatestBlock RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» block_id|object|false|none|none|
|»» hash|string(byte)|false|none|none|
|»» part_set_header|object|false|none|none|
|»»» total|integer(int64)|false|none|none|
|»»» hash|string(byte)|false|none|none|
|» block|object|false|none|none|
|»» header|object|false|none|Header defines the structure of a Tendermint block header.|
|»»» version|object|false|none|Consensus captures the consensus rules for processing a block in the blockchain,including all blockchain data structures and the rules of the application'sstate transition machine.|
|»»»» block|string(uint64)|false|none|none|
|»»»» app|string(uint64)|false|none|none|
|»»» chain_id|string|false|none|none|
|»»» height|string(int64)|false|none|none|
|»»» time|string(date-time)|false|none|none|
|»»» last_block_id|object|false|none|none|
|»»»» hash|string(byte)|false|none|none|
|»»»» part_set_header|object|false|none|none|
|»»»»» total|integer(int64)|false|none|none|
|»»»»» hash|string(byte)|false|none|none|
|»»» last_commit_hash|string(byte)|false|none|commit from validators from the last block|
|»»» data_hash|string(byte)|false|none|none|
|»»» validators_hash|string(byte)|false|none|validators for the current block|
|»»» next_validators_hash|string(byte)|false|none|none|
|»»» consensus_hash|string(byte)|false|none|none|
|»»» app_hash|string(byte)|false|none|none|
|»»» last_results_hash|string(byte)|false|none|none|
|»»» evidence_hash|string(byte)|false|none|evidence included in the block|
|»»» proposer_address|string(byte)|false|none|none|
|»» data|object|false|none|none|
|»»» txs|[string]|false|none|Txs that will be applied by state @ block.Height+1.NOTE: not all txs here are valid.  We're just agreeing on the order first.This means that block.AppHash does not include these txs.|
|»» evidence|object|false|none|none|
|»»» evidence|[object]|false|none|none|
|»»»» duplicate_vote_evidence|object|false|none|DuplicateVoteEvidence contains evidence of a validator signed two conflicting votes.|
|»»»»» vote_a|object|false|none|Vote represents a prevote, precommit, or commit vote from validators forconsensus.|
|»»»»»» type|string|false|none|SignedMsgType is a type of signed message in the consensus. - SIGNED_MSG_TYPE_PREVOTE: Votes - SIGNED_MSG_TYPE_PROPOSAL: Proposals|
|»»»»»» height|string(int64)|false|none|none|
|»»»»»» round|integer(int32)|false|none|none|
|»»»»»» block_id|object|false|none|zero if vote is nil.|
|»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»» timestamp|string(date-time)|false|none|none|
|»»»»»» validator_address|string(byte)|false|none|none|
|»»»»»» validator_index|integer(int32)|false|none|none|
|»»»»»» signature|string(byte)|false|none|none|
|»»»»» vote_b|object|false|none|Vote represents a prevote, precommit, or commit vote from validators forconsensus.|
|»»»»»» type|string|false|none|SignedMsgType is a type of signed message in the consensus. - SIGNED_MSG_TYPE_PREVOTE: Votes - SIGNED_MSG_TYPE_PROPOSAL: Proposals|
|»»»»»» height|string(int64)|false|none|none|
|»»»»»» round|integer(int32)|false|none|none|
|»»»»»» block_id|object|false|none|zero if vote is nil.|
|»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»» timestamp|string(date-time)|false|none|none|
|»»»»»» validator_address|string(byte)|false|none|none|
|»»»»»» validator_index|integer(int32)|false|none|none|
|»»»»»» signature|string(byte)|false|none|none|
|»»»»» total_voting_power|string(int64)|false|none|none|
|»»»»» validator_power|string(int64)|false|none|none|
|»»»»» timestamp|string(date-time)|false|none|none|
|»»»» light_client_attack_evidence|object|false|none|LightClientAttackEvidence contains evidence of a set of validators attempting to mislead a light client.|
|»»»»» conflicting_block|object|false|none|none|
|»»»»»» signed_header|object|false|none|none|
|»»»»»»» header|object|false|none|Header defines the structure of a Tendermint block header.|
|»»»»»»»» version|object|false|none|Consensus captures the consensus rules for processing a block in the blockchain,including all blockchain data structures and the rules of the application'sstate transition machine.|
|»»»»»»»»» block|string(uint64)|false|none|none|
|»»»»»»»»» app|string(uint64)|false|none|none|
|»»»»»»»» chain_id|string|false|none|none|
|»»»»»»»» height|string(int64)|false|none|none|
|»»»»»»»» time|string(date-time)|false|none|none|
|»»»»»»»» last_block_id|object|false|none|none|
|»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»» last_commit_hash|string(byte)|false|none|commit from validators from the last block|
|»»»»»»»» data_hash|string(byte)|false|none|none|
|»»»»»»»» validators_hash|string(byte)|false|none|validators for the current block|
|»»»»»»»» next_validators_hash|string(byte)|false|none|none|
|»»»»»»»» consensus_hash|string(byte)|false|none|none|
|»»»»»»»» app_hash|string(byte)|false|none|none|
|»»»»»»»» last_results_hash|string(byte)|false|none|none|
|»»»»»»»» evidence_hash|string(byte)|false|none|evidence included in the block|
|»»»»»»»» proposer_address|string(byte)|false|none|none|
|»»»»»»» commit|object|false|none|Commit contains the evidence that a block was committed by a set of validators.|
|»»»»»»»» height|string(int64)|false|none|none|
|»»»»»»»» round|integer(int32)|false|none|none|
|»»»»»»»» block_id|object|false|none|none|
|»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»» signatures|[object]|false|none|none|
|»»»»»»»»» block_id_flag|string|false|none|none|
|»»»»»»»»» validator_address|string(byte)|false|none|none|
|»»»»»»»»» timestamp|string(date-time)|false|none|none|
|»»»»»»»»» signature|string(byte)|false|none|none|
|»»»»»» validator_set|object|false|none|none|
|»»»»»»» validators|[object]|false|none|none|
|»»»»»»»» address|string(byte)|false|none|none|
|»»»»»»»» pub_key|object|false|none|none|
|»»»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»»»» proposer|object|false|none|none|
|»»»»»»»» address|string(byte)|false|none|none|
|»»»»»»»» pub_key|object|false|none|none|
|»»»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»»»» total_voting_power|string(int64)|false|none|none|
|»»»»» common_height|string(int64)|false|none|none|
|»»»»» byzantine_validators|[object]|false|none|none|
|»»»»»» address|string(byte)|false|none|none|
|»»»»»» pub_key|object|false|none|none|
|»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»» total_voting_power|string(int64)|false|none|none|
|»»»»» timestamp|string(date-time)|false|none|none|
|»» last_commit|object|false|none|Commit contains the evidence that a block was committed by a set of validators.|
|»»» height|string(int64)|false|none|none|
|»»» round|integer(int32)|false|none|none|
|»»» block_id|object|false|none|none|
|»»»» hash|string(byte)|false|none|none|
|»»»» part_set_header|object|false|none|none|
|»»»»» total|integer(int64)|false|none|none|
|»»»»» hash|string(byte)|false|none|none|
|»»» signatures|[object]|false|none|none|
|»»»» block_id_flag|string|false|none|none|
|»»»» validator_address|string(byte)|false|none|none|
|»»»» timestamp|string(date-time)|false|none|none|
|»»»» signature|string(byte)|false|none|none|

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

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## CosmosBaseTendermintV1Beta1GetBlockByHeight

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/blocks/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/blocks/string', {

> The result from the above endpoint looks like this:

```json
{
  "block_id": {
    "hash": "0x1234567890abcdef...",
    "part_set_header": {
      "total": 0,
      "hash": "0x1234567890abcdef..."
    }
  },
  "block": {
    "header": {
      "version": {
        "block": "1000000",
        "app": "1000000"
      },
      "chain_id": "0x1234567890abcdef...",
      "height": "height..."
    },
    "data": {
      "txs": [
        "item..."
      ]
    },
    "evidence": {
      "evidence": [
        {
          "duplicate_vote_evidence": {
            "vote_a": {
              "type": "type...",
              "height": "height...",
              "round": 0
            },
            "vote_b": {
              "type": "type...",
              "height": "height...",
              "round": 0
            },
            "total_voting_power": "total_voting_power..."
          },
          "light_client_attack_evidence": {
            "conflicting_block": {
              "signed_header": {
                "header": {
                  "version": {
                    "block": "1000000",
                    "app": "1000000"
                  },
                  "chain_id": "0x1234567890abcdef...",
                  "height": "height..."
                },
                "commit": {
                  "height": "height...",
                  "round": 0,
                  "block_id": {
                    "hash": "0x1234567890abcdef...",
                    "part_set_header": {
                      "total": 0,
                      "hash": "0x1234567890abcdef..."
                    }
                  }
                }
              },
              "validator_set": {
                "validators": [
                  {
                    "address": "0x1234567890abcdef...",
                    "pub_key": {
                      "ed25519": "ed25519...",
                      "secp256k1": "secp256k1..."
                    },
                    "voting_power": "voting_power..."
                  }
                ],
                "proposer": {
                  "address": "0x1234567890abcdef...",
                  "pub_key": {
                    "ed25519": "ed25519...",
                    "secp256k1": "secp256k1..."
                  },
                  "voting_power": "voting_power..."
                },
                "total_voting_power": "total_voting_power..."
              }
            },
            "common_height": "common_height...",
            "byzantine_validators": [
              {
                "address": "0x1234567890abcdef...",
                "pub_key": {
                  "ed25519": "ed25519...",
                  "secp256k1": "secp256k1..."
                },
                "voting_power": "voting_power..."
              }
            ]
          }
        }
      ]
    }
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

`GET /cosmos/base/tendermint/v1beta1/blocks/{height}`

*GetBlockByHeight queries block for given height.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|height|path|string(int64)|true|none|

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*GetBlockByHeightResponse is the response type for the Query/GetBlockByHeight RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» block_id|object|false|none|none|
|»» hash|string(byte)|false|none|none|
|»» part_set_header|object|false|none|none|
|»»» total|integer(int64)|false|none|none|
|»»» hash|string(byte)|false|none|none|
|» block|object|false|none|none|
|»» header|object|false|none|Header defines the structure of a Tendermint block header.|
|»»» version|object|false|none|Consensus captures the consensus rules for processing a block in the blockchain,including all blockchain data structures and the rules of the application'sstate transition machine.|
|»»»» block|string(uint64)|false|none|none|
|»»»» app|string(uint64)|false|none|none|
|»»» chain_id|string|false|none|none|
|»»» height|string(int64)|false|none|none|
|»»» time|string(date-time)|false|none|none|
|»»» last_block_id|object|false|none|none|
|»»»» hash|string(byte)|false|none|none|
|»»»» part_set_header|object|false|none|none|
|»»»»» total|integer(int64)|false|none|none|
|»»»»» hash|string(byte)|false|none|none|
|»»» last_commit_hash|string(byte)|false|none|commit from validators from the last block|
|»»» data_hash|string(byte)|false|none|none|
|»»» validators_hash|string(byte)|false|none|validators for the current block|
|»»» next_validators_hash|string(byte)|false|none|none|
|»»» consensus_hash|string(byte)|false|none|none|
|»»» app_hash|string(byte)|false|none|none|
|»»» last_results_hash|string(byte)|false|none|none|
|»»» evidence_hash|string(byte)|false|none|evidence included in the block|
|»»» proposer_address|string(byte)|false|none|none|
|»» data|object|false|none|none|
|»»» txs|[string]|false|none|Txs that will be applied by state @ block.Height+1.NOTE: not all txs here are valid.  We're just agreeing on the order first.This means that block.AppHash does not include these txs.|
|»» evidence|object|false|none|none|
|»»» evidence|[object]|false|none|none|
|»»»» duplicate_vote_evidence|object|false|none|DuplicateVoteEvidence contains evidence of a validator signed two conflicting votes.|
|»»»»» vote_a|object|false|none|Vote represents a prevote, precommit, or commit vote from validators forconsensus.|
|»»»»»» type|string|false|none|SignedMsgType is a type of signed message in the consensus. - SIGNED_MSG_TYPE_PREVOTE: Votes - SIGNED_MSG_TYPE_PROPOSAL: Proposals|
|»»»»»» height|string(int64)|false|none|none|
|»»»»»» round|integer(int32)|false|none|none|
|»»»»»» block_id|object|false|none|zero if vote is nil.|
|»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»» timestamp|string(date-time)|false|none|none|
|»»»»»» validator_address|string(byte)|false|none|none|
|»»»»»» validator_index|integer(int32)|false|none|none|
|»»»»»» signature|string(byte)|false|none|none|
|»»»»» vote_b|object|false|none|Vote represents a prevote, precommit, or commit vote from validators forconsensus.|
|»»»»»» type|string|false|none|SignedMsgType is a type of signed message in the consensus. - SIGNED_MSG_TYPE_PREVOTE: Votes - SIGNED_MSG_TYPE_PROPOSAL: Proposals|
|»»»»»» height|string(int64)|false|none|none|
|»»»»»» round|integer(int32)|false|none|none|
|»»»»»» block_id|object|false|none|zero if vote is nil.|
|»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»» timestamp|string(date-time)|false|none|none|
|»»»»»» validator_address|string(byte)|false|none|none|
|»»»»»» validator_index|integer(int32)|false|none|none|
|»»»»»» signature|string(byte)|false|none|none|
|»»»»» total_voting_power|string(int64)|false|none|none|
|»»»»» validator_power|string(int64)|false|none|none|
|»»»»» timestamp|string(date-time)|false|none|none|
|»»»» light_client_attack_evidence|object|false|none|LightClientAttackEvidence contains evidence of a set of validators attempting to mislead a light client.|
|»»»»» conflicting_block|object|false|none|none|
|»»»»»» signed_header|object|false|none|none|
|»»»»»»» header|object|false|none|Header defines the structure of a Tendermint block header.|
|»»»»»»»» version|object|false|none|Consensus captures the consensus rules for processing a block in the blockchain,including all blockchain data structures and the rules of the application'sstate transition machine.|
|»»»»»»»»» block|string(uint64)|false|none|none|
|»»»»»»»»» app|string(uint64)|false|none|none|
|»»»»»»»» chain_id|string|false|none|none|
|»»»»»»»» height|string(int64)|false|none|none|
|»»»»»»»» time|string(date-time)|false|none|none|
|»»»»»»»» last_block_id|object|false|none|none|
|»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»» last_commit_hash|string(byte)|false|none|commit from validators from the last block|
|»»»»»»»» data_hash|string(byte)|false|none|none|
|»»»»»»»» validators_hash|string(byte)|false|none|validators for the current block|
|»»»»»»»» next_validators_hash|string(byte)|false|none|none|
|»»»»»»»» consensus_hash|string(byte)|false|none|none|
|»»»»»»»» app_hash|string(byte)|false|none|none|
|»»»»»»»» last_results_hash|string(byte)|false|none|none|
|»»»»»»»» evidence_hash|string(byte)|false|none|evidence included in the block|
|»»»»»»»» proposer_address|string(byte)|false|none|none|
|»»»»»»» commit|object|false|none|Commit contains the evidence that a block was committed by a set of validators.|
|»»»»»»»» height|string(int64)|false|none|none|
|»»»»»»»» round|integer(int32)|false|none|none|
|»»»»»»»» block_id|object|false|none|none|
|»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»»» part_set_header|object|false|none|none|
|»»»»»»»»»» total|integer(int64)|false|none|none|
|»»»»»»»»»» hash|string(byte)|false|none|none|
|»»»»»»»» signatures|[object]|false|none|none|
|»»»»»»»»» block_id_flag|string|false|none|none|
|»»»»»»»»» validator_address|string(byte)|false|none|none|
|»»»»»»»»» timestamp|string(date-time)|false|none|none|
|»»»»»»»»» signature|string(byte)|false|none|none|
|»»»»»» validator_set|object|false|none|none|
|»»»»»»» validators|[object]|false|none|none|
|»»»»»»»» address|string(byte)|false|none|none|
|»»»»»»»» pub_key|object|false|none|none|
|»»»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»»»» proposer|object|false|none|none|
|»»»»»»»» address|string(byte)|false|none|none|
|»»»»»»»» pub_key|object|false|none|none|
|»»»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»»»» total_voting_power|string(int64)|false|none|none|
|»»»»» common_height|string(int64)|false|none|none|
|»»»»» byzantine_validators|[object]|false|none|none|
|»»»»»» address|string(byte)|false|none|none|
|»»»»»» pub_key|object|false|none|none|
|»»»»»»» ed25519|string(byte)|false|none|none|
|»»»»»»» secp256k1|string(byte)|false|none|none|
|»»»»»» voting_power|string(int64)|false|none|none|
|»»»»»» proposer_priority|string(int64)|false|none|none|
|»»»»» total_voting_power|string(int64)|false|none|none|
|»»»»» timestamp|string(date-time)|false|none|none|
|»» last_commit|object|false|none|Commit contains the evidence that a block was committed by a set of validators.|
|»»» height|string(int64)|false|none|none|
|»»» round|integer(int32)|false|none|none|
|»»» block_id|object|false|none|none|
|»»»» hash|string(byte)|false|none|none|
|»»»» part_set_header|object|false|none|none|
|»»»»» total|integer(int64)|false|none|none|
|»»»»» hash|string(byte)|false|none|none|
|»»» signatures|[object]|false|none|none|
|»»»» block_id_flag|string|false|none|none|
|»»»» validator_address|string(byte)|false|none|none|
|»»»» timestamp|string(date-time)|false|none|none|
|»»»» signature|string(byte)|false|none|none|

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

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer(int32)|false|none|none|
|» message|string|false|none|none|
|» details|[object]|false|none|none|
|»» **additionalProperties**|any|false|none|none|
|»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|

> This operation does not require authentication

## CosmosBaseTendermintV1Beta1GetNodeInfo

> Code samples

```shell

> The result from the above endpoint looks like this:

```json
{
  "default_node_info": {
    "protocol_version": {
      "p2p": "1000000",
      "block": "1000000",
      "app": "1000000"
    },
    "default_node_id": "0x1234567890abcdef...",
    "listen_addr": "listen_addr..."
  },
  "application_version": {
    "name": "name...",
    "app_name": "app_name...",
    "version": "version..."
  }
}
```

curl --request GET \
  --url https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/node_info \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/node_info', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/base/tendermint/v1beta1/node_info`

*GetNodeInfo queries the current node info.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*GetNodeInfoResponse is the request type for the Query/GetNodeInfo RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» default_node_info|object|false|none|none|
|»» protocol_version|object|false|none|none|
|»»» p2p|string(uint64)|false|none|none|
|»»» block|string(uint64)|false|none|none|
|»»» app|string(uint64)|false|none|none|
|»» default_node_id|string|false|none|none|
|»» listen_addr|string|false|none|none|
|»» network|string|false|none|none|
|»» version|string|false|none|none|
|»» channels|string(byte)|false|none|none|
|»» moniker|string|false|none|none|
|»» other|object|false|none|none|
|»»» tx_index|string|false|none|none|
|»»» rpc_address|string|false|none|none|
|» application_version|object|false|none|VersionInfo is the type for the GetNodeInfoResponse message.|
|»» name|string|false|none|none|
|»» app_name|string|false|none|none|
|»» version|string|false|none|none|
|»» git_commit|string|false|none|none|
|»» build_tags|string|false|none|none|
|»» go_version|string|false|none|none|
|»» build_deps|[object]|false|none|none|
|»»» Module is the type for VersionInfo|object|false|none|none|
|»»»» path|string|false|none|none|
|»»»» version|string|false|none|none|
|»»»» sum|string|false|none|none|
|»» cosmos_sdk_version|string|false|none|none|

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
  "syncing": true
}
```

> This operation does not require authentication

## CosmosBaseTendermintV1Beta1GetSyncing

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/syncing \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/syncing', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/base/tendermint/v1beta1/syncing`

*GetSyncing queries node syncing.*

> Example responses

> 200 Response

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A successful response.|Inline|
|default|Default|An unexpected error response.|Inline|

### Response Schema

Status Code **200**

*GetSyncingResponse is the response type for the Query/GetSyncing RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» syncing|boolean|false|none|none|

Status Code **default**

|Name|Type|Required|Restrictions|Description|

> The result from the above endpoint looks like this:

```json
{
  "block_height": "block_height...",
  "validators": [
    {
      "address": "0x1234567890abcdef...",
      "pub_key": {
        "@type": "@type..."
      },
      "voting_power": "voting_power..."
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
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

## CosmosBaseTendermintV1Beta1GetLatestValidatorSet

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/validatorsets/latest \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/validatorsets/latest', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/base/tendermint/v1beta1/validatorsets/latest`

*GetLatestValidatorSet queries latest validator-set.*

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

*GetLatestValidatorSetResponse is the response type for the Query/GetValidatorSetByHeight RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» block_height|string(int64)|false|none|none|
|» validators|[object]|false|none|none|
|»» address|string|false|none|none|
|»» pub_key|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» voting_power|string(int64)|false|none|none|
|»» proposer_priority|string(int64)|false|none|none|

> The result from the above endpoint looks like this:

```json
{
  "block_height": "block_height...",
  "validators": [
    {
      "address": "0x1234567890abcdef...",
      "pub_key": {
        "@type": "@type..."
      },
      "voting_power": "voting_power..."
    }
  ],
  "pagination": {
    "next_key": "next_key...",
    "total": "1000000"
  }
}
```

|» pagination|object|false|none|pagination defines an pagination for the response.|
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

## CosmosBaseTendermintV1Beta1GetValidatorSetByHeight

> Code samples

```shell
curl --request GET \
  --url https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/validatorsets/string \
  --header 'Accept: */*'
```

```javascript
const response = await fetch('https://lcd.twilight.org/cosmos/base/tendermint/v1beta1/validatorsets/string', {
  headers: {
    'Accept': '*/*'
  }
});
const data = await response.json();
console.log(data);
```

`GET /cosmos/base/tendermint/v1beta1/validatorsets/{height}`

*GetValidatorSetByHeight queries validator-set at a given height.*

### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|height|path|string(int64)|true|none|
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

*GetValidatorSetByHeightResponse is the response type for the Query/GetValidatorSetByHeight RPC method.*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» block_height|string(int64)|false|none|none|
|» validators|[object]|false|none|none|
|»» address|string|false|none|none|
|»» pub_key|object|false|none|`Any` contains an arbitrary serialized protocol buffer message along with aURL that describes the type of the serialized message.Protobuf library provides support to pack/unpack Any values in the formof utility functions or additional generated methods of the Any type.Example 1: Pack and unpack a message in C++.    Foo foo = ...;    Any any;    any.PackFrom(foo);    ...    if (any.UnpackTo(&foo)) {      ...    }Example 2: Pack and unpack a message in Java.    Foo foo = ...;    Any any = Any.pack(foo);    ...    if (any.is(Foo.class)) {      foo = any.unpack(Foo.class);    } Example 3: Pack and unpack a message in Python.    foo = Foo(...)    any = Any()    any.Pack(foo)    ...    if any.Is(Foo.DESCRIPTOR):      any.Unpack(foo)      ... Example 4: Pack and unpack a message in Go     foo := &pb.Foo{...}     any, err := anypb.New(foo)     if err != nil {       ...     }     ...     foo := &pb.Foo{}     if err := any.UnmarshalTo(foo); err != nil {       ...     }The pack methods provided by protobuf library will by default use'type.googleapis.com/full.type.name' as the type URL and the unpackmethods only use the fully qualified type name after the last '/'in the type URL, for example "foo.bar.com/x/y.z" will yield typename "y.z".JSON====The JSON representation of an `Any` value uses the regularrepresentation of the deserialized, embedded message, with anadditional field `@type` which contains the type URL. Example:    package google.profile;    message Person {      string first_name = 1;      string last_name = 2;    }    {      "@type": "type.googleapis.com/google.profile.Person",      "firstName": ,      "lastName":     }If the embedded message type is well-known and has a custom JSONrepresentation, that representation will be embedded adding a field`value` which holds the custom JSON in addition to the `@type`field. Example (for message [google.protobuf.Duration][]):    {      "@type": "type.googleapis.com/google.protobuf.Duration",      "value": "1.212s"    }|
|»»» **additionalProperties**|any|false|none|none|
|»»» @type|string|false|none|A URL/resource name that uniquely identifies the type of the serializedprotocol buffer message. This string must contain at leastone "/" character. The last segment of the URL's path must representthe fully qualified name of the type (as in`path/google.protobuf.Duration`). The name should be in a canonical form(e.g., leading "." is not accepted).In practice, teams usually precompile into the binary all types that theyexpect it to use in the context of Any. However, for URLs which use thescheme `http`, `https`, or no scheme, one can optionally set up a typeserver that maps type URLs to message definitions as follows:* If no scheme is provided, `https` is assumed.* An HTTP GET on the URL must yield a [google.protobuf.Type][]  value in binary format, or produce an error.* Applications are allowed to cache lookup results based on the  URL, or have them precompiled into a binary to avoid any  lookup. Therefore, binary compatibility needs to be preserved  on changes to types. (Use versioned type names to manage  breaking changes.)Note: this functionality is not currently available in the officialprotobuf release, and it is not used for type URLs beginning withtype.googleapis.com.Schemes other than `http`, `https` (or the empty scheme) might beused with implementation specific semantics.|
|»» voting_power|string(int64)|false|none|none|
|»» proposer_priority|string(int64)|false|none|none|
|» pagination|object|false|none|pagination defines an pagination for the response.|
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
