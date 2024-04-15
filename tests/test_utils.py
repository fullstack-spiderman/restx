import json
from datetime import timedelta
from typing import Any, Literal

import pytest
from pytest_httpx import HTTPXMock

from restx.enums import HTTPMethod
from restx.utils import crud_manager

URL: str = "https://example.com/users"


def assert_crud_manager(
    httpx_mock: HTTPXMock,
    http_method: HTTPMethod,
    url: str,
    payload: str,
    disable_ssl_verify: bool,
    follow_redirects: bool,
    status_code: Literal[200] | Literal[201] | Literal[204],
) -> None:
    # Arrange
    headers: dict[str, str] = {"Authorization": "Bearer token"}
    response_data: dict[str, str] = {"status": "success"}
    httpx_mock.add_response(
        method=http_method.value, status_code=status_code, url=url, json=response_data
    )

    # Act
    result_without_options: dict[str, Any] = crud_manager(
        url=url,
        method=http_method.value,
        headers=json.dumps(headers),
        disable_ssl_verify=disable_ssl_verify,
        follow_redirects=follow_redirects,
        payload=payload,
    )

    # Assert
    assert result_without_options["response"].status_code == status_code
    assert isinstance(result_without_options["response_time"], timedelta)
    assert result_without_options["response"].json() == response_data


@pytest.mark.parametrize(
    "http_method, url, payload, disable_ssl_verify, follow_redirects, status_code",
    [
        (HTTPMethod.GET, URL, None, False, False, 200),
        (
            HTTPMethod.POST,
            URL,
            '{"key": "value"}',
            False,
            False,
            201,
        ),
        (
            HTTPMethod.PUT,
            f"{URL}/1",
            '{"key": "value"}',
            False,
            False,
            200,
        ),
        (
            HTTPMethod.PATCH,
            f"{URL}/1",
            '{"key": "value"}',
            False,
            False,
            200,
        ),
        (HTTPMethod.DELETE, f"{URL}/1", None, False, False, 204),
        (HTTPMethod.GET, f"{URL}/", None, True, True, 200),
        (
            HTTPMethod.POST,
            f"{URL}/",
            '{"key": "value"}',
            True,
            True,
            201,
        ),
        (
            HTTPMethod.PUT,
            f"{URL}/1/",
            '{"key": "value"}',
            True,
            True,
            200,
        ),
        (
            HTTPMethod.PATCH,
            f"{URL}/1/",
            '{"key": "value"}',
            True,
            True,
            200,
        ),
        (HTTPMethod.DELETE, f"{URL}/1/", None, True, True, 204),
    ],
    ids=[
        "GET - Users - Default SSL - No Redirects",
        "POST - Users - Default SSL - No Redirects",
        "PUT - Patch User - Default SSL - No Redirects",
        "PATCH - User - Default SSL - No Redirects",
        "DELETE - User - Default SSL - No Redirects",
        "GET - Users - Disable SSL - Follow Redirects",
        "POST - Users - Disable SSL - Follow Redirects",
        "PUT - Patch User - Disable SSL - Follow Redirects",
        "PATCH - User - Disable SSL - Follow Redirects",
        "DELETE - User - Disable SSL - Follow Redirects",
    ],
)
def test_crud_manager(
    httpx_mock: HTTPXMock,
    http_method: HTTPMethod,
    url: str,
    payload: str,
    disable_ssl_verify: bool,
    follow_redirects: bool,
    status_code: Literal[200] | Literal[201] | Literal[204],
) -> None:
    assert_crud_manager(
        httpx_mock=httpx_mock,
        http_method=http_method,
        url=url,
        payload=payload,
        disable_ssl_verify=disable_ssl_verify,
        follow_redirects=follow_redirects,
        status_code=status_code,
    )
