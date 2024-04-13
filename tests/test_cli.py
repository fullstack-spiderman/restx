from crud.cli import get

from pytest_httpx import HTTPXMock


def test_get(httpx_mock: HTTPXMock) -> None:
    # Arrange
    response_data: dict[str, str] = {"key": "value"}
    httpx_mock.add_response(url="https://example.com", json=response_data)
    url = "https://example.com"

    # Act
    get(url)

    # Assert
    assert len(httpx_mock.get_requests()) == 1
    assert httpx_mock.get_requests()[0].url == url
