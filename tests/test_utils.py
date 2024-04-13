from datetime import timedelta
from typing import Any, Generator

import pytest
from pytest_httpx import HTTPXMock

import restx
import restx.enums
from restx.utils import crud_manager


@pytest.fixture
def mock_client(httpx_mock: HTTPXMock) -> Generator[HTTPXMock, None, None]:
    yield httpx_mock


def test_crud_manager_get(httpx_mock: HTTPXMock) -> None:
    # Arrange
    url = "https://example.com"
    headers: dict[str, str] = {"Authorization": "Bearer token"}
    response_data: dict[str, str] = {"status": "success"}
    httpx_mock.add_response(method="GET", status_code=200, url=url, json=response_data)

    # Act
    result: dict[str, Any] = crud_manager(
        url=url, method=restx.enums.HTTPMethod.GET.value, headers=headers
    )

    # Assert
    assert result["response"].status_code == 200
    assert isinstance(result["response_time"], timedelta)
    assert result["response"].json() == response_data
