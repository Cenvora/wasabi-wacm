"""Mixin containing WACM standalone account endpoints."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from requests import Response

from ._base import EndpointMixin


class StandaloneAccountEndpoints(EndpointMixin):
    """Operations for `/v1/accounts` resources."""

    def get_storage_amounts(self) -> Response:
        """GET /v1/accounts/storage-amounts"""

        return self._request("GET", "/v1/accounts/storage-amounts")

    def create_standalone_account(self, payload: Mapping[str, Any]) -> Response:
        """POST /v1/accounts"""

        return self._request("POST", "/v1/accounts", json=payload)

    def get_standalone_accounts(
        self,
        *,
        id_: Optional[str | int] = None,
        name: Optional[str] = None,
        email: Optional[str] = None,
        status: Optional[str] = None,
        wasabi_account_number: Optional[str | int] = None,
        page: Optional[int] = None,
        size: Optional[int] = None,
        partner_name: Optional[str] = None,
        storage_amount: Optional[str | int] = None,
        company_name: Optional[str] = None,
    ) -> Response:
        """GET /v1/accounts"""

        params = {
            "id": id_,
            "name": name,
            "email": email,
            "status": status,
            "wasabiAccountNumber": wasabi_account_number,
            "page": page,
            "size": size,
            "partnerName": partner_name,
            "storageAmount": storage_amount,
            "companyName": company_name,
        }
        return self._request("GET", "/v1/accounts", params=params)

    def get_countries(self) -> Response:
        """GET /v1/accounts/countries"""

        return self._request("GET", "/v1/accounts/countries")


__all__ = ["StandaloneAccountEndpoints"]
