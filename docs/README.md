# WACM Python Client

This module wraps the **Wasabi Account Control Manager (WACM)** REST API using the official Postman collection (`docs/WACM Connect.postman_collection.json`) as the source of truth. It provides thin convenience helpers around `requests` so you can interact with the API without copying request payloads or URLs.

---

## Installation

The client lives inside this repository. If you want to re-use it in your own project you can either

```bash
pip install -e .
```

or add the `wasabi` package directory to your Python path.

The runtime dependency list is intentionally minimal:

- [`requests`](https://docs.python-requests.org/) – HTTP transport and authentication helpers

---

## Getting Started

```python
from wasabi.wacm import WACMClient

client = WACMClient(
    username="your-basic-auth-username",
    password="your-basic-auth-password",
    # optional overrides:
    # base_url="https://api.wacm.wasabisys.com/api",
    # timeout=30,
)

response = client.get_sub_accounts(page=1, size=20)
print(response.json())
```

You can also use the client as a context manager to make sure the underlying `requests.Session` is closed promptly:

```python
from wasabi.wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    accounts = client.get_sub_accounts()
    print(accounts.json())
```

---

## Authentication

The Postman collection uses *Basic Auth* credentials. When you instantiate `WACMClient` with `username` and `password`, the client configures a [`HTTPBasicAuth`](https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication) object automatically. You can supply your own `requests.auth.AuthBase` implementation via the optional `auth` argument if you need more control.

---

## Client Structure

The client is composed of several mixins, split by resource family. This keeps the code base approachable and mirrors the Postman folders:

- `SubAccountEndpoints`
- `MemberEndpoints`
- `ChannelAccountEndpoints`
- `StandaloneAccountEndpoints`
- `UsageEndpoints`
- `InvoiceEndpoints`
- `ControlAccountEndpoints`

Every public method maps directly to a request in the Postman collection. Query parameters have sensible defaults and are normalised so that `None` values are omitted and `bool` values serialise to lowercase strings (as expected by the API).

The full list of methods is available by inspecting `wasabi/wacm/client.py` or via tools like `dir(WACMClient)` in a Python shell.

---

## Handling Errors

Any non-successful HTTP response raises a `WACMRequestError`. The exception includes the original `requests.Response` instance for inspection:

```python
from wasabi.wacm import WACMClient, WACMRequestError

client = WACMClient(username="user", password="bad-password")

try:
    client.get_sub_accounts()
except WACMRequestError as exc:
    print(exc)
    print(exc.response.status_code)
    print(exc.response.text)
```

---

## Advanced Configuration

`WACMClient` accepts a few optional arguments:

- `base_url` – override the API root (defaults to `https://api.wacm.wasabisys.com/api`)
- `timeout` – float or `(connect_timeout, read_timeout)` tuple passed to `requests`
- `session` – provide your own configured `requests.Session`
- `auth` – supply a custom `AuthBase` implementation; useful if you rely on bearer tokens or signed requests

All requests share the same session, making it simple to configure retries or proxies once:

```python
import requests
from wasabi.wacm import WACMClient

session = requests.Session()
session.proxies = {"https": "http://proxy.local:3128"}

client = WACMClient(username="user", password="secret", session=session)
```

---

## Example Workflow

```python
from wasabi.wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    # Create a sub-account
    payload = {
        "controlAccountId": 3732,
        "name": "sample-sub-account",
        "wasabiAccountEmail": "noreply@example.com",
        "password": "StrongPassword!",
    }
    create_response = client.create_sub_account(payload)
    sub_account = create_response.json()

    # Fetch usage for the new sub-account
    usages = client.get_usages(sub_account_id=sub_account["id"])
    print(usages.json())
```

---

## Development Notes

- The code in `wasabi/wacm` is generated manually from the Postman collection and designed for clarity, not heavy abstraction.
- The helper function in `base.py` ensures query parameter cleaning is consistent across endpoints.
- If the Postman collection changes, update the relevant mixin and keep the rest of the structure intact.

### Class Reference
- [BaseWACMClient](classes/base_client.md)
- [WACMClient](classes/wacm_client.md)
- [WACMRequestError](classes/exceptions.md)
- [SubAccountEndpoints](classes/sub_account_endpoints.md)
- [MemberEndpoints](classes/member_endpoints.md)
- [ChannelAccountEndpoints](classes/channel_account_endpoints.md)
- [StandaloneAccountEndpoints](classes/standalone_account_endpoints.md)
- [UsageEndpoints](classes/usage_endpoints.md)
- [InvoiceEndpoints](classes/invoice_endpoints.md)
- [ControlAccountEndpoints](classes/control_account_endpoints.md)

---

## Further Reading

- [Wasabi Account Control Manager documentation](https://wasabi-support.zendesk.com/hc/en-us/articles/10408387708699-Account-Control-Manager)
- [Requests documentation](https://requests.readthedocs.io/en/latest/)
