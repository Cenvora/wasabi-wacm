# MemberEndpoints

## Overview
`MemberEndpoints` provides helpers for the `/v1/members` portion of the WACM API. Use these methods through `WACMClient` to manage sub-account members.

## Methods
| Method | HTTP | Path | Key query params |
| --- | --- | --- | --- |
| `create_member(payload)` | POST | `/v1/members` | – |
| `get_members(...)` | GET | `/v1/members` | `page`, `size`, `id`, `status`, `username`, `subAccountId` |
| `get_member(member_id)` | GET | `/v1/members/{id}` | – |
| `update_member(member_id, payload)` | PUT | `/v1/members/{id}` | – |
| `delete_member(member_id)` | DELETE | `/v1/members/{id}` | – |

## Usage Examples
List active members for a sub-account:

```python
from wasabi.wacm import WACMClient

client = WACMClient(username="user", password="secret")
active_members = client.get_members(status="Active", sub_account_id=32455)
print(active_members.json())
```

Update a member profile:

```python
from wasabi.wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    payload = {"status": "Suspended"}
    client.update_member(member_id=9876, payload=payload)
```
