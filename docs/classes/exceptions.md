# WACMRequestError

## Overview
`WACMRequestError` is raised whenever the underlying HTTP request returns a non-success status code. It inherits from `RuntimeError` and stores the original `requests.Response` object for further inspection.

```python
from wasabi.wacm import WACMClient, WACMRequestError

client = WACMClient(username="user", password="secret")
try:
    client.get_invoice("non-existent")
except WACMRequestError as exc:
    print(exc)                 # Human-readable error message
    print(exc.response.status_code)
    print(exc.response.text)
```

## Attributes
- `response`: the `requests.Response` instance that triggered the exception. Use it to read headers, parse JSON, or inspect error bodies.

## When To Catch
- Retrying or falling back to a different credential source.
- Logging detailed diagnostics without crashing a worker process.
- Translating API errors into domain-specific exceptions for upstream callers.

## Raising Custom Errors
If you build your own mixins, re-use `WACMRequestError` to keep error handling consistent:

```python
from wasabi.wacm.exceptions import WACMRequestError

try:
    response = client._request("GET", "/v1/custom")
except WACMRequestError as exc:
    handle(exc.response)
```
