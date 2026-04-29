# BaseWACMClient

## Overview
`BaseWACMClient` supplies the shared HTTP plumbing that every endpoint mixin relies on. It configures a reusable `requests.Session`, normalises query parameters, and provides the protected `_request()` helper that the mixins call.

You normally do not instantiate `BaseWACMClient` directly, but understanding its knobs helps you customise the concrete `WACMClient`.

## Initialisation Arguments
- `base_url`: Root of the WACM API. Defaults to `https://api.wacm.wasabisys.com/api` and is normalised to remove a trailing slash.
- `username` / `password`: Optional basic-auth credentials. When both are supplied the client configures `requests.auth.HTTPBasicAuth` automatically.
- `auth`: Optional `requests.auth.AuthBase` instance. Use this to override the basic auth behaviour (for example, to provide bearer tokens).
- `session`: Optional pre-configured `requests.Session`. Supply your own if you need custom adapters, retry policies, or proxies.
- `timeout`: Either a float or a `(connect_timeout, read_timeout)` tuple passed straight to `requests`.

## Lifecycle
`BaseWACMClient` implements context manager hooks so you can use `with` blocks to guarantee `Session.close()` is invoked:

```python
from wasabi.wacm.base import BaseWACMClient

with BaseWACMClient(username="user", password="secret") as base:
    response = base._request("GET", "/v1/accounts/countries")
    print(response.json())
```

> ℹ️  `_request()` is considered an internal helper; prefer the higher-level methods on `WACMClient` unless you are extending the package.

## Extending the Client
If you need to add additional endpoint groups, subclass `BaseWACMClient` together with your own mixin:

```python
from wasabi.wacm.base import BaseWACMClient

class CustomEndpointMixin:
    def get_health(self):
        return self._request("GET", "/v1/health")

class CustomClient(BaseWACMClient, CustomEndpointMixin):
    """Adds a custom health check to the stock client."""

client = CustomClient(username="user", password="secret")
print(client.get_health().json())
```

This pattern mirrors the structure used for the built-in endpoint mixins.
