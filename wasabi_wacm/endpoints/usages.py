"""Mixin containing WACM usage endpoints."""

from __future__ import annotations

from typing import Optional

from requests import Response

from ._base import EndpointMixin


class UsageEndpoints(EndpointMixin):
    """Operations for `/v1/usages` resources."""

    def get_usages(
        self,
        *,
        page: Optional[int] = None,
        size: Optional[int] = None,
        governance_account_id: Optional[str | int] = None,
        control_account_id: Optional[str | int] = None,
        sub_account_id: Optional[str | int] = None,
        latest: Optional[bool] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        wasabi_account_number: Optional[str | int] = None,
    ) -> Response:
        """GET /v1/usages"""

        params = {
            "page": page,
            "size": size,
            "governanceAccountId": governance_account_id,
            "controlAccountId": control_account_id,
            "subAccountId": sub_account_id,
            "latest": latest,
            "from": from_,
            "to": to,
            "wasabiAccountNumber": wasabi_account_number,
        }
        return self._request("GET", "/v1/usages", params=params)

    def get_usage(self, utilization_id: str | int) -> Response:
        """GET /v1/usages/:utilizationId"""

        path = f"/v1/usages/{utilization_id}"
        return self._request("GET", path)


__all__ = ["UsageEndpoints"]
