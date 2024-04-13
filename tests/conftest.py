from typing import Generator

import pytest
from pytest_httpx import HTTPXMock


@pytest.fixture
def mock_client(httpx_mock: HTTPXMock) -> Generator[HTTPXMock, None, None]:
    yield httpx_mock
