<p align="center">
  <img src="media/wasabi-logo.svg" alt="Wasabi logo" height="80">
</p>

<h1 align="center">wasabi-wacm</h1>

<p align="center">
  Python client utilities for the Wasabi Account Control Manager API.
</p>

This project provides a small, synchronous Python wrapper around the Wasabi Account Control Manager (WACM) REST API. It uses `requests`, exposes one `WACMClient`, and keeps responses as raw `requests.Response` objects so callers can decide how to parse and handle API payloads.

This is an independent open source project. It is not affiliated with, endorsed by, or sponsored by Wasabi Technologies.

## Features

- Basic-auth configuration from `username` and `password`
- Reusable `requests.Session` with context-manager support
- Endpoint helpers for control accounts, channel accounts, sub-accounts, standalone accounts, members, invoices, and usage
- Automatic omission of `None` query parameters
- Lowercase boolean query parameter serialisation for WACM-compatible URLs
- `WACMRequestError` wrapper that preserves the original `requests.Response`

## Requirements

- Python 3.9 or later
- `requests`
- Access to a Wasabi Account Control Manager account and API credentials

## Installation

Install from source:

```bash
git clone https://github.com/Cenvora/wasabi-wacm.git
cd wasabi-wacm
pip install -e .
```

When a release is available from PyPI or your internal package index, install the configured package name with:

```bash
pip install wasabi-wacm
```

For development dependencies:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from wasabi_wacm import WACMClient

with WACMClient(
    username="your-basic-auth-username",
    password="your-basic-auth-password",
) as client:
    response = client.get_sub_accounts(page=1, size=20)
    print(response.json())
```

By default, the client uses:

```text
https://api.wacm.wasabisys.com/api
```

Override it when you need to target another WACM API root:

```python
from wasabi_wacm import WACMClient

client = WACMClient(
    base_url="https://api.wacm.wasabisys.com/api",
    username="your-basic-auth-username",
    password="your-basic-auth-password",
    timeout=30,
)
```

## Authentication

WACM API access commonly uses HTTP Basic Auth. Passing `username` and `password` configures `requests.auth.HTTPBasicAuth` automatically:

```python
from wasabi_wacm import WACMClient

client = WACMClient(username="user", password="secret")
```

If you need custom authentication, pass any `requests.auth.AuthBase` instance:

```python
import requests

from wasabi_wacm import WACMClient


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token: str) -> None:
        self.token = token

    def __call__(self, request: requests.PreparedRequest) -> requests.PreparedRequest:
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request


client = WACMClient(auth=BearerAuth("token"))
```

## Usage Examples

List sub-accounts:

```python
from wasabi_wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    sub_accounts = client.get_sub_accounts(
        page=1,
        size=50,
        include_deleted=False,
        include_keys=False,
    ).json()
```

Fetch latest usage for a sub-account:

```python
from wasabi_wacm import WACMClient

with WACMClient(username="user", password="secret") as client:
    usage = client.get_usages(
        sub_account_id=12345,
        latest=True,
    ).json()
```

Create a sub-account:

```python
from wasabi_wacm import WACMClient

payload = {
    "controlAccountId": 3732,
    "name": "example-sub-account",
    "wasabiAccountEmail": "storage-admin@example.com",
    "password": "change-me",
}

with WACMClient(username="user", password="secret") as client:
    created = client.create_sub_account(payload).json()
    print(created)
```

Configure a shared session:

```python
import requests

from wasabi_wacm import WACMClient

session = requests.Session()
session.proxies = {"https": "http://proxy.example.com:3128"}

with WACMClient(username="user", password="secret", session=session) as client:
    countries = client.get_countries().json()
```

## Supported Endpoint Groups

| Area | Methods |
| --- | --- |
| Channel accounts | `create_channel_account`, `create_channel_account_user`, `get_channel_accounts`, `get_channel_account`, `update_channel_account`, `delete_channel_account_user`, `delete_channel_account` |
| Control accounts | `get_control_accounts`, `get_control_account`, `get_control_account_usage`, `get_control_account_bucket_utilization` |
| Invoices | `get_invoices`, `get_invoice` |
| Members | `create_member`, `get_members`, `get_member`, `update_member`, `delete_member` |
| Standalone accounts | `create_standalone_account`, `get_standalone_accounts`, `get_storage_amounts`, `get_countries` |
| Sub-accounts | `create_sub_account`, `get_sub_accounts`, `get_sub_account`, `update_sub_account`, `patch_sub_account`, `delete_sub_account`, `get_sub_account_bucket_utilization` |
| Usage | `get_usages`, `get_usage` |

All endpoint methods return a `requests.Response`. Use `.json()`, `.text`, `.content`, or other `requests` response APIs depending on the endpoint.

## Error Handling

`response.raise_for_status()` is called internally. Non-successful HTTP responses are wrapped in `WACMRequestError`, and the original response remains available on the exception:

```python
from wasabi_wacm import WACMClient, WACMRequestError

try:
    with WACMClient(username="user", password="bad-password") as client:
        client.get_sub_accounts()
except WACMRequestError as exc:
    print(exc)
    print(exc.response.status_code)
    print(exc.response.text)
```

## Development

Run the test suite:

```bash
pytest
```

Run type checking:

```bash
mypy wasabi_wacm
```

The public client is composed from focused endpoint mixins under `wasabi_wacm/endpoints`. When adding WACM operations, prefer adding the method to the resource-specific mixin and exposing it through `WACMClient` via `wasabi_wacm/endpoints/__init__.py`.

## Documentation

- [Wasabi Account Control Manager documentation](https://docs.wasabi.com/docs/wacm-wasabi-account-control-manager)
- [Wasabi Account Control API reference](https://docs.wasabi.com/apidocs/partner-api)
- [Requests documentation](https://requests.readthedocs.io/en/latest/)

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

Wasabi, Wasabi Account Control Manager, and the Wasabi logo are trademarks of Wasabi Technologies. The logo asset in this repository was downloaded from wasabi.com and is used only to identify the third-party service targeted by this client.

## Contributors

- [Jonah May](https://github.com/JonahMMay)
- [Maurice Kevenaar](https://github.com/mkevenaar)
