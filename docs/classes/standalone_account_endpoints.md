# StandaloneAccountEndpoints

## Overview
`StandaloneAccountEndpoints` covers the `/v1/accounts` family of endpoints used to manage standalone (non-channel) accounts.

## Methods
| Method | HTTP | Path | Key query params |
| --- | --- | --- | --- |
| `get_storage_amounts()` | GET | `/v1/accounts/storage-amounts` | – |
| `create_standalone_account(payload)` | POST | `/v1/accounts` | – |
| `get_standalone_accounts(...)` | GET | `/v1/accounts` | `id`, `name`, `email`, `status`, `wasabiAccountNumber`, `page`, `size`, `partnerName`, `storageAmount`, `companyName` |
| `get_countries()` | GET | `/v1/accounts/countries` | – |

## Usage Examples
Fetch available storage quotas:

```python
from wasabi.wacm import WACMClient

client = WACMClient(username="user", password="secret")
options = client.get_storage_amounts().json()
print(options)
```

Search for pending standalone accounts:

```python
pending_accounts = client.get_standalone_accounts(status="Pending", page=1, size=50)
print(pending_accounts.json())
```
