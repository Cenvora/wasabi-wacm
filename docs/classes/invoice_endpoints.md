# InvoiceEndpoints

## Overview
`InvoiceEndpoints` contains helper methods for the `/v1/invoices` API surface.

## Methods
| Method | HTTP | Path | Key query params |
| --- | --- | --- | --- |
| `get_invoices(...)` | GET | `/v1/invoices` | `page`, `size`, `id`, `governanceAccountId`, `controlAccountId`, `subAccountId`, `controlInvoiceId`, `latest`, `from`, `to`, `subInvoiceId`, `wasabiAccountNumber` |
| `get_invoice(invoice_id)` | GET | `/v1/invoices/{invoiceId}` | – |

## Usage Examples
Retrieve the latest invoices for a control account:

```python
from wasabi.wacm import WACMClient

client = WACMClient(username="user", password="secret")
invoices = client.get_invoices(control_account_id=13338, latest=True)
print(invoices.json())
```

Fetch a single invoice by ID:

```python
invoice = client.get_invoice(invoice_id=4321)
print(invoice.json())
```
