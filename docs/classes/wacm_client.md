# WACMClient

## Overview
`WACMClient` is the public entry point that combines `BaseWACMClient` with all endpoint mixins. Each method corresponds to a request in the Postman collection shipped with this repo (`docs/WACM Connect.postman_collection.json`).

```python
from wasabi.wacm import WACMClient

client = WACMClient(username="user", password="secret")
sub_accounts = client.get_sub_accounts(page=1, size=20)
print(sub_accounts.json())
```

## Composition
`WACMClient` inherits the following mixins:

- `SubAccountEndpoints`
- `MemberEndpoints`
- `ChannelAccountEndpoints`
- `StandaloneAccountEndpoints`
- `UsageEndpoints`
- `InvoiceEndpoints`
- `ControlAccountEndpoints`

This means your editor or IDE can surface every available method via auto-completion on a single object.

## Common Patterns
- **Session reuse** – The client keeps one `requests.Session` for all calls. Use the `session` argument to inject retries or proxies.
- **Context manager** – `with WACMClient(...) as client:` ensures the session is closed automatically.
- **Chaining calls** – Because each method returns a raw `requests.Response`, you can decide whether to call `.json()`, `.text`, or stream the payload.

## Example Workflow
```python
from wasabi.wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    # 1. Create a sub-account
    payload = {
        "controlAccountId": 3732,
        "name": "sample-sub-account",
        "wasabiAccountEmail": "noreply@example.com",
        "password": "StrongPassword!",
    }
    sub_account = client.create_sub_account(payload).json()

    # 2. Look up invoices for the new sub-account
    invoices = client.get_invoices(sub_account_id=sub_account["id"]).json()

    # 3. Fetch usage data
    usage = client.get_usages(sub_account_id=sub_account["id"], latest=True).json()

    print(len(invoices), usage)
```

## Error Handling
All methods raise `WACMRequestError` on non-successful HTTP responses. Catch the exception to inspect the underlying `requests.Response`:

```python
from wasabi.wacm import WACMClient, WACMRequestError

client = WACMClient(username="user", password="wrong")
try:
    client.get_sub_accounts()
except WACMRequestError as exc:
    print(exc.response.status_code)
    print(exc.response.text)
```
