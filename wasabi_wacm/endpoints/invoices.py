"""Mixin containing WACM invoice endpoints."""

from __future__ import annotations

from typing import Optional

from requests import Response

from ._base import EndpointMixin


class InvoiceEndpoints(EndpointMixin):
    """Operations for `/v1/invoices` resources."""

    def get_invoices(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        id_: Optional[str | int] = None,
        governance_account_id: Optional[str | int] = None,
        control_account_id: Optional[str | int] = None,
        sub_account_id: Optional[str | int] = None,
        control_invoice_id: Optional[str | int] = None,
        latest: Optional[bool] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        sub_invoice_id: Optional[str | int] = None,
        wasabi_account_number: Optional[str | int] = None,
    ) -> Response:
        """GET /v1/invoices"""

        params = {
            "page": page,
            "size": size,
            "id": id_,
            "governanceAccountId": governance_account_id,
            "controlAccountId": control_account_id,
            "subAccountId": sub_account_id,
            "controlInvoiceId": control_invoice_id,
            "latest": latest,
            "from": from_,
            "to": to,
            "subInvoiceId": sub_invoice_id,
            "wasabiAccountNumber": wasabi_account_number,
        }
        return self._request("GET", "/v1/invoices", params=params)

    def get_invoice(self, invoice_id: str | int) -> Response:
        """GET /v1/invoices/:invoiceId"""

        path = f"/v1/invoices/{invoice_id}"
        return self._request("GET", path)


__all__ = ["InvoiceEndpoints"]
