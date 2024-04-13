import json
from datetime import datetime, timedelta
from typing import Any

from httpx import Client, Response

from labs.cli import HTTPMethod

DEFAULT_METHOD = "GET"


def crud_manager(
    url: str,
    payload=None,
    headers=None,
    method: str = DEFAULT_METHOD,
) -> dict[str, Any]:
    """Perform an HTTP request based on the user choice."""
    start_time: datetime = datetime.now()
    CHOICE: str = method.upper()
    with Client() as client:
        if CHOICE == HTTPMethod.GET.value:
            response: Response = client.get(url, headers=headers)
        elif CHOICE == HTTPMethod.POST.value:
            response: Response = client.post(
                url, json=json.loads(payload), headers=headers
            )
        elif CHOICE == HTTPMethod.PUT.value:
            response: Response = client.put(
                url, json=json.loads(payload), headers=headers
            )
        elif CHOICE == HTTPMethod.PATCH.value:
            response: Response = client.patch(
                url, json=json.loads(payload), headers=headers
            )
        elif CHOICE == HTTPMethod.DELETE.value:
            response: Response = client.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
    end_time: datetime = datetime.now()
    response_time: timedelta = end_time - start_time
    return {"response": response, "response_time": response_time}


def format_response(response: Response, response_time) -> dict[str, Any]:
    """Format the response information."""
    return {
        "Status Code": response.status_code,
        "HTTP Method": response.request.method,
        "URL": response.url,
        "Response Time": response_time,
        "Headers": response.headers,
        "Body": response.json(),
    }
