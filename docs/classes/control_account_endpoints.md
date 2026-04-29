# ControlAccountEndpoints

## Overview
`ControlAccountEndpoints` works with the `/v1/control-accounts` resources, including usage and bucket utilisation views that aggregate sub-account data.

## Methods
| Method | HTTP | Path | Key query params |
| --- | --- | --- | --- |
| `get_control_account_usage(...)` | GET | `/v1/control-accounts/usages` | `page`, `size`, `governanceAccountId`, `controlAccountId`, `latest`, `from`, `to`, `wasabiAccountNumber` |
| `get_control_accounts(...)` | GET | `/v1/control-accounts` | `page`, `size`, `name`, `governanceAccountId`, `status`, `primaryApiKey`, `includeApiKey`, `id`, `controlAccountEmail`, `includeDeleted`, `includeDeletedSubAccounts` |
| `get_control_account(control_account_id, ...)` | GET | `/v1/control-accounts/{controlAccountId}` | `includeDeleted`, `includeDeletedSubAccounts` |
| `get_control_account_bucket_utilization(control_account_id, ...)` | GET | `/v1/control-accounts/{controlAccountId}/buckets` | `page`, `size`, `from`, `to`, `latest`, `name`, `bucketNumber`, `region` |

## Usage Examples
Enumerate control accounts including soft-deleted ones:

```python
from wasabi.wacm import WACMClient

client = WACMClient(username="user", password="secret")
accounts = client.get_control_accounts(include_deleted=True, include_deleted_sub_accounts=True)
print(accounts.json())
```

Inspect bucket utilisation for a control account:

```python
with WACMClient(username="user", password="secret") as client:
    buckets = client.get_control_account_bucket_utilization(
        control_account_id=13455,
        latest=True,
        region="us-east-1",
    )
    print(buckets.json())
```
