# UsageEndpoints

## Overview
`UsageEndpoints` provides read-only helpers for the `/v1/usages` endpoints that surface utilisation metrics.

## Methods
| Method | HTTP | Path | Key query params |
| --- | --- | --- | --- |
| `get_usages(...)` | GET | `/v1/usages` | `page`, `size`, `governanceAccountId`, `controlAccountId`, `subAccountId`, `latest`, `from`, `to`, `wasabiAccountNumber` |
| `get_usage(utilization_id)` | GET | `/v1/usages/{utilizationId}` | – |

## Usage Examples
Pull the latest readings for a sub-account:

```python
from wasabi.wacm import WACMClient

usage = WACMClient(username="user", password="secret").get_usages(
    sub_account_id=234,
    latest=True,
)
print(usage.json())
```

Fetch a specific utilisation record:

```python
client = WACMClient(username="user", password="secret")
record = client.get_usage(utilization_id=99887766).json()
print(record)
```
