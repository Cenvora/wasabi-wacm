# ChannelAccountEndpoints

## Overview
`ChannelAccountEndpoints` encapsulates every `/v1/channel-accounts` request. Use these helpers to manage resellers and their associated users.

## Methods
| Method | HTTP | Path | Key query params |
| --- | --- | --- | --- |
| `create_channel_account(payload)` | POST | `/v1/channel-accounts` | – |
| `create_channel_account_user(payload)` | POST | `/v1/channel-accounts/users` | – |
| `get_channel_accounts(...)` | GET | `/v1/channel-accounts` | `page`, `size`, `id`, `status`, `name`, `contactEmail`, `controlAccountId`, `includeDeletedSubAccounts` |
| `get_channel_account(channel_account_id, ...)` | GET | `/v1/channel-accounts/{channelAccountId}` | `includeDeletedSubAccounts` |
| `update_channel_account(channel_account_id, payload)` | PUT | `/v1/channel-accounts/{channelAccountId}` | – |
| `delete_channel_account_user(user_id)` | DELETE | `/v1/channel-accounts/users/{userId}` | – |
| `delete_channel_account(account_id)` | DELETE | `/v1/channel-accounts/{id}` | – |

## Usage Examples
Create a channel account and invite a user:

```python
from wasabi.wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    account_payload = {"name": "Acme Reseller", "contactEmail": "ops@acme.example"}
    account = client.create_channel_account(account_payload).json()

    user_payload = {"channelAccountId": account["id"], "email": "owner@acme.example"}
    client.create_channel_account_user(user_payload)
```

List channel accounts including deleted sub-accounts:

```python
accounts = client.get_channel_accounts(include_deleted_sub_accounts=True)
print(accounts.json())
```
