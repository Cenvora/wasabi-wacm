# SubAccountEndpoints

## Overview
`SubAccountEndpoints` groups every `/v1/sub-accounts` request from the Postman collection. The mixin is included in `WACMClient`, so you typically access these methods through that class.

## Methods
| Method | HTTP | Path | Key query params |
| --- | --- | --- | --- |
| `create_sub_account(payload)` | POST | `/v1/sub-accounts` | – |
| `get_sub_account_bucket_utilization(sub_account_id, ...)` | GET | `/v1/sub-accounts/{subAccountId}/buckets` | `page`, `size`, `from`, `to`, `latest`, `name`, `bucketNumber`, `region` |
| `get_sub_accounts(...)` | GET | `/v1/sub-accounts` | `page`, `size`, `id`, `name`, `controlAccountId`, `governanceAccountId`, `status`, `wasabiAccountName`, `wasabiAccountNumber`, `includeDeleted`, `includeKeys` |
| `get_sub_account(sub_account_id, ...)` | GET | `/v1/sub-accounts/{subAccountId}` | `includeKeys` |
| `update_sub_account(sub_account_id, payload, ...)` | PUT | `/v1/sub-accounts/{id}` | `includeKeys` |
| `patch_sub_account(sub_account_id, payload, ...)` | PATCH | `/v1/sub-accounts/{id}` | `includeKeys` |
| `delete_sub_account(sub_account_id)` | DELETE | `/v1/sub-accounts/{id}` | – |

> All methods return a `requests.Response`. Call `.json()` to parse JSON bodies.

## Usage Examples
Create a sub-account and immediately fetch it:

```python
from wasabi.wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    payload = {
        "controlAccountId": 3732,
        "name": "sample-sub-account",
        "wasabiAccountEmail": "noreply@example.com",
        "password": "StrongPassword!",
    }
    created = client.create_sub_account(payload).json()

    sub_account = client.get_sub_account(created["id"], include_keys=True).json()
    print(sub_account)
```

Fetch bucket utilisation metrics:

```python
from wasabi.wacm import WACMClient

client = WACMClient(username="user", password="secret")
utilisation = client.get_sub_account_bucket_utilization(
    sub_account_id=1234,
    latest=True,
    region="us-east-1",
)
print(utilisation.json())
```
