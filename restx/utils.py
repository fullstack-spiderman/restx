import json
from datetime import datetime, timedelta
from typing import Any

from httpx import Client, Response
from rich import box
from rich.console import Console
from rich.table import Table

from restx.enums import HTTPMethod

console = Console()
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
            response: Response = client.get(
                url,
                headers=json.loads(headers) if headers else headers,
            )
        elif CHOICE == HTTPMethod.POST.value:
            response: Response = client.post(
                url,
                json=json.loads(payload),
                headers=json.loads(headers) if headers else headers,
            )
        elif CHOICE == HTTPMethod.PUT.value:
            response: Response = client.put(
                url,
                json=json.loads(payload),
                headers=json.loads(headers) if headers else headers,
            )
        elif CHOICE == HTTPMethod.PATCH.value:
            response: Response = client.patch(
                url,
                json=json.loads(payload),
                headers=json.loads(headers) if headers else headers,
            )
        elif CHOICE == HTTPMethod.DELETE.value:
            response: Response = client.delete(
                url,
                headers=json.loads(headers) if headers else headers,
            )
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


def print_additional_info(response: Response, response_time) -> None:
    """Print additional information at the top."""
    additional_info: str = f"Status Code: {response.status_code}\nHTTP Method: {response.request.method}\nURL: {response.url}\nResponse Time: {response_time}\nHeaders: {response.headers}\n\n"
    console.print(additional_info, style="bold magenta")


def print_response_headers(response: Response) -> None:
    console.rule("[bold]Response Headers[/bold]", style="blue", align="center")

    table = Table(box=box.SQUARE)
    table.add_column("Header", style="cyan", justify="right")
    table.add_column("Value", justify="left")

    for name, value in response.headers.items():
        table.add_row(f"{name}:", value)

    console.print(table)


def print_response_body(response: Response) -> None:
    console.rule("[bold]Response Body[/bold]", style="blue", align="center")
    try:
        body = json.loads(response.text)
        formatted_body: str = json.dumps(body, indent=4)
        console.print(formatted_body)
    except json.JSONDecodeError:
        console.print(response.text)
