import json
from datetime import timedelta
from typing import Any

from pytest_httpx import HTTPXMock

from restx.enums import HTTPMethod
from restx.utils import crud_manager


def test_crud_manager_get(httpx_mock: HTTPXMock) -> None:
    # Arrange
    url = "https://example.com"
    headers: dict[str, str] = {"Authorization": "Bearer token"}
    response_data: dict[str, str] = {"status": "success"}
    httpx_mock.add_response(method="GET", status_code=200, url=url, json=response_data)

    # Act
    result: dict[str, Any] = crud_manager(
        url=url, method=HTTPMethod.GET.value, headers=json.dumps(headers)
    )

    # Assert
    assert result["response"].status_code == 200
    assert isinstance(result["response_time"], timedelta)
    assert result["response"].json() == response_data


def test_crud_manager_post(httpx_mock: HTTPXMock) -> None:
    # Arrange
    url = "https://example.com"
    payload: dict[str, str] = {"key": "value"}
    headers: dict[str, str] = {"Authorization": "Bearer token"}
    response_data: dict[str, str] = {"status": "success"}
    httpx_mock.add_response(method="POST", status_code=201, url=url, json=response_data)

    # Act
    result: dict[str, Any] = crud_manager(
        url=url,
        method=HTTPMethod.POST.value,
        payload=json.dumps(payload),
        headers=json.dumps(headers),
    )

    # Assert
    assert result["response"].status_code == 201
    assert isinstance(result["response_time"], timedelta)
    assert result["response"].json() == response_data


def test_crud_manager_put(httpx_mock: HTTPXMock) -> None:
    # Arrange
    url = "https://example.com/5"
    payload: dict[str, str] = {"key": "value"}
    headers: dict[str, str] = {"Authorization": "Bearer token"}
    response_data: dict[str, str] = {"status": "success"}
    httpx_mock.add_response(method="PUT", status_code=200, url=url, json=response_data)

    # Act
    result: dict[str, Any] = crud_manager(
        url=url,
        method=HTTPMethod.PUT.value,
        payload=json.dumps(payload),
        headers=json.dumps(headers),
    )

    # Assert
    assert result["response"].status_code == 200
    assert isinstance(result["response_time"], timedelta)
    assert result["response"].json() == response_data


def test_crud_manager_patch(httpx_mock: HTTPXMock) -> None:
    # Arrange
    url = "https://example.com/13"
    payload: dict[str, str] = {"key": "value"}
    headers: dict[str, str] = {"Authorization": "Bearer token"}
    response_data: dict[str, str] = {"status": "success"}
    httpx_mock.add_response(
        method="PATCH", status_code=200, url=url, json=response_data
    )

    # Act
    result: dict[str, Any] = crud_manager(
        url=url,
        method=HTTPMethod.PATCH.value,
        payload=json.dumps(payload),
        headers=json.dumps(headers),
    )

    # Assert
    assert result["response"].status_code == 200
    assert isinstance(result["response_time"], timedelta)
    assert result["response"].json() == response_data
