from __future__ import annotations

from typing import Any, Callable

import pytest
from requests import Response

from wasabi_wacm import WACMClient


class RecordingWACMClient(WACMClient):
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []
        self.response = Response()

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
    ) -> Response:
        call: dict[str, Any] = {"method": method, "path": path}
        if params is not None:
            call["params"] = params
        if json is not None:
            call["json"] = json
        self.calls.append(call)
        return self.response


EndpointCall = Callable[[RecordingWACMClient], Response]


@pytest.mark.parametrize(
    ("operation", "expected"),
    [
        pytest.param(
            lambda client: client.create_channel_account({"name": "channel"}),
            {
                "method": "POST",
                "path": "/v1/channel-accounts",
                "json": {"name": "channel"},
            },
            id="create_channel_account",
        ),
        pytest.param(
            lambda client: client.create_channel_account_user({"email": "user@example.com"}),
            {
                "method": "POST",
                "path": "/v1/channel-accounts/users",
                "json": {"email": "user@example.com"},
            },
            id="create_channel_account_user",
        ),
        pytest.param(
            lambda client: client.get_channel_accounts(
                page=1,
                size=50,
                id_=123,
                status="active",
                name="channel",
                contact_email="owner@example.com",
                control_account_id=456,
                include_deleted_sub_accounts=True,
            ),
            {
                "method": "GET",
                "path": "/v1/channel-accounts",
                "params": {
                    "page": 1,
                    "size": 50,
                    "id": 123,
                    "status": "active",
                    "name": "channel",
                    "contactEmail": "owner@example.com",
                    "controlAccountId": 456,
                    "includeDeletedSubAccounts": True,
                },
            },
            id="get_channel_accounts",
        ),
        pytest.param(
            lambda client: client.get_channel_account(123, include_deleted_sub_accounts=False),
            {
                "method": "GET",
                "path": "/v1/channel-accounts/123",
                "params": {"includeDeletedSubAccounts": False},
            },
            id="get_channel_account",
        ),
        pytest.param(
            lambda client: client.update_channel_account(123, {"name": "updated"}),
            {
                "method": "PUT",
                "path": "/v1/channel-accounts/123",
                "json": {"name": "updated"},
            },
            id="update_channel_account",
        ),
        pytest.param(
            lambda client: client.delete_channel_account_user(789),
            {"method": "DELETE", "path": "/v1/channel-accounts/users/789"},
            id="delete_channel_account_user",
        ),
        pytest.param(
            lambda client: client.delete_channel_account(123),
            {"method": "DELETE", "path": "/v1/channel-accounts/123"},
            id="delete_channel_account",
        ),
        pytest.param(
            lambda client: client.get_control_account_usage(
                page=2,
                size=25,
                governance_account_id=11,
                control_account_id=22,
                latest=True,
                from_="2026-01-01",
                to="2026-01-31",
                wasabi_account_number=333,
            ),
            {
                "method": "GET",
                "path": "/v1/control-accounts/usages",
                "params": {
                    "page": 2,
                    "size": 25,
                    "governanceAccountId": 11,
                    "controlAccountId": 22,
                    "latest": True,
                    "from": "2026-01-01",
                    "to": "2026-01-31",
                    "wasabiAccountNumber": 333,
                },
            },
            id="get_control_account_usage",
        ),
        pytest.param(
            lambda client: client.get_control_accounts(
                page=1,
                size=20,
                name="control",
                governance_account_id=11,
                status="active",
                primary_api_key="key",
                include_api_key=True,
                id_=22,
                control_account_email="control@example.com",
                include_deleted=False,
                include_deleted_sub_accounts=True,
            ),
            {
                "method": "GET",
                "path": "/v1/control-accounts",
                "params": {
                    "page": 1,
                    "size": 20,
                    "name": "control",
                    "governanceAccountId": 11,
                    "status": "active",
                    "primaryApiKey": "key",
                    "includeApiKey": True,
                    "id": 22,
                    "controlAccountEmail": "control@example.com",
                    "includeDeleted": False,
                    "includeDeletedSubAccounts": True,
                },
            },
            id="get_control_accounts",
        ),
        pytest.param(
            lambda client: client.get_control_account(
                22,
                include_deleted=False,
                include_deleted_sub_accounts=True,
            ),
            {
                "method": "GET",
                "path": "/v1/control-accounts/22",
                "params": {
                    "includeDeleted": False,
                    "includeDeletedSubAccounts": True,
                },
            },
            id="get_control_account",
        ),
        pytest.param(
            lambda client: client.get_control_account_bucket_utilization(
                22,
                page=1,
                size=10,
                from_="2026-01-01",
                to="2026-01-31",
                latest=True,
                name="bucket",
                bucket_number=44,
                region="us-east-1",
            ),
            {
                "method": "GET",
                "path": "/v1/control-accounts/22/buckets",
                "params": {
                    "page": 1,
                    "size": 10,
                    "from": "2026-01-01",
                    "to": "2026-01-31",
                    "latest": True,
                    "name": "bucket",
                    "bucketNumber": 44,
                    "region": "us-east-1",
                },
            },
            id="get_control_account_bucket_utilization",
        ),
        pytest.param(
            lambda client: client.get_invoices(
                page=1,
                size=25,
                id_=101,
                governance_account_id=11,
                control_account_id=22,
                sub_account_id=33,
                control_invoice_id=44,
                latest=True,
                from_="2026-01-01",
                to="2026-01-31",
                sub_invoice_id=55,
                wasabi_account_number=66,
            ),
            {
                "method": "GET",
                "path": "/v1/invoices",
                "params": {
                    "page": 1,
                    "size": 25,
                    "id": 101,
                    "governanceAccountId": 11,
                    "controlAccountId": 22,
                    "subAccountId": 33,
                    "controlInvoiceId": 44,
                    "latest": True,
                    "from": "2026-01-01",
                    "to": "2026-01-31",
                    "subInvoiceId": 55,
                    "wasabiAccountNumber": 66,
                },
            },
            id="get_invoices",
        ),
        pytest.param(
            lambda client: client.get_invoice(101),
            {"method": "GET", "path": "/v1/invoices/101"},
            id="get_invoice",
        ),
        pytest.param(
            lambda client: client.create_member({"username": "member"}),
            {
                "method": "POST",
                "path": "/v1/members",
                "json": {"username": "member"},
            },
            id="create_member",
        ),
        pytest.param(
            lambda client: client.get_members(
                page=1,
                size=10,
                id_=7,
                status="active",
                username="member",
                sub_account_id=33,
            ),
            {
                "method": "GET",
                "path": "/v1/members",
                "params": {
                    "page": 1,
                    "size": 10,
                    "id": 7,
                    "status": "active",
                    "username": "member",
                    "subAccountId": 33,
                },
            },
            id="get_members",
        ),
        pytest.param(
            lambda client: client.get_member(7),
            {"method": "GET", "path": "/v1/members/7"},
            id="get_member",
        ),
        pytest.param(
            lambda client: client.update_member(7, {"username": "updated"}),
            {
                "method": "PUT",
                "path": "/v1/members/7",
                "json": {"username": "updated"},
            },
            id="update_member",
        ),
        pytest.param(
            lambda client: client.delete_member(7),
            {"method": "DELETE", "path": "/v1/members/7"},
            id="delete_member",
        ),
        pytest.param(
            lambda client: client.get_storage_amounts(),
            {"method": "GET", "path": "/v1/accounts/storage-amounts"},
            id="get_storage_amounts",
        ),
        pytest.param(
            lambda client: client.create_standalone_account({"name": "standalone"}),
            {
                "method": "POST",
                "path": "/v1/accounts",
                "json": {"name": "standalone"},
            },
            id="create_standalone_account",
        ),
        pytest.param(
            lambda client: client.get_standalone_accounts(
                id_=5,
                name="standalone",
                email="standalone@example.com",
                status="active",
                wasabi_account_number=6,
                page=1,
                size=15,
                partner_name="partner",
                storage_amount=1024,
                company_name="Example Inc",
            ),
            {
                "method": "GET",
                "path": "/v1/accounts",
                "params": {
                    "id": 5,
                    "name": "standalone",
                    "email": "standalone@example.com",
                    "status": "active",
                    "wasabiAccountNumber": 6,
                    "page": 1,
                    "size": 15,
                    "partnerName": "partner",
                    "storageAmount": 1024,
                    "companyName": "Example Inc",
                },
            },
            id="get_standalone_accounts",
        ),
        pytest.param(
            lambda client: client.get_countries(),
            {"method": "GET", "path": "/v1/accounts/countries"},
            id="get_countries",
        ),
        pytest.param(
            lambda client: client.create_sub_account({"name": "sub"}),
            {
                "method": "POST",
                "path": "/v1/sub-accounts",
                "json": {"name": "sub"},
            },
            id="create_sub_account",
        ),
        pytest.param(
            lambda client: client.get_sub_account_bucket_utilization(
                33,
                page=1,
                size=10,
                from_="2026-01-01",
                to="2026-01-31",
                latest=True,
                name="bucket",
                bucket_number=44,
                region="us-east-1",
            ),
            {
                "method": "GET",
                "path": "/v1/sub-accounts/33/buckets",
                "params": {
                    "page": 1,
                    "size": 10,
                    "from": "2026-01-01",
                    "to": "2026-01-31",
                    "latest": True,
                    "name": "bucket",
                    "bucketNumber": 44,
                    "region": "us-east-1",
                },
            },
            id="get_sub_account_bucket_utilization",
        ),
        pytest.param(
            lambda client: client.get_sub_accounts(
                page=1,
                size=50,
                id_=33,
                name="sub",
                control_account_id=22,
                governance_account_id=11,
                status="active",
                wasabi_account_name="wasabi-sub",
                wasabi_account_number=66,
                include_deleted=False,
                include_keys=True,
            ),
            {
                "method": "GET",
                "path": "/v1/sub-accounts",
                "params": {
                    "page": 1,
                    "size": 50,
                    "id": 33,
                    "name": "sub",
                    "controlAccountId": 22,
                    "governanceAccountId": 11,
                    "status": "active",
                    "wasabiAccountName": "wasabi-sub",
                    "wasabiAccountNumber": 66,
                    "includeDeleted": False,
                    "includeKeys": True,
                },
            },
            id="get_sub_accounts",
        ),
        pytest.param(
            lambda client: client.get_sub_account(33, include_keys=True),
            {
                "method": "GET",
                "path": "/v1/sub-accounts/33",
                "params": {"includeKeys": True},
            },
            id="get_sub_account",
        ),
        pytest.param(
            lambda client: client.update_sub_account(33, {"name": "updated"}, include_keys=False),
            {
                "method": "PUT",
                "path": "/v1/sub-accounts/33",
                "params": {"includeKeys": False},
                "json": {"name": "updated"},
            },
            id="update_sub_account",
        ),
        pytest.param(
            lambda client: client.patch_sub_account(33, {"status": "active"}, include_keys=True),
            {
                "method": "PATCH",
                "path": "/v1/sub-accounts/33",
                "params": {"includeKeys": True},
                "json": {"status": "active"},
            },
            id="patch_sub_account",
        ),
        pytest.param(
            lambda client: client.delete_sub_account(33),
            {"method": "DELETE", "path": "/v1/sub-accounts/33"},
            id="delete_sub_account",
        ),
        pytest.param(
            lambda client: client.get_usages(
                page=1,
                size=25,
                governance_account_id=11,
                control_account_id=22,
                sub_account_id=33,
                latest=True,
                from_="2026-01-01",
                to="2026-01-31",
                wasabi_account_number=66,
            ),
            {
                "method": "GET",
                "path": "/v1/usages",
                "params": {
                    "page": 1,
                    "size": 25,
                    "governanceAccountId": 11,
                    "controlAccountId": 22,
                    "subAccountId": 33,
                    "latest": True,
                    "from": "2026-01-01",
                    "to": "2026-01-31",
                    "wasabiAccountNumber": 66,
                },
            },
            id="get_usages",
        ),
        pytest.param(
            lambda client: client.get_usage(99),
            {"method": "GET", "path": "/v1/usages/99"},
            id="get_usage",
        ),
    ],
)
def test_endpoint_methods_issue_expected_request(
    operation: EndpointCall,
    expected: dict[str, Any],
) -> None:
    client = RecordingWACMClient()

    result = operation(client)

    assert result is client.response
    assert client.calls == [expected]
