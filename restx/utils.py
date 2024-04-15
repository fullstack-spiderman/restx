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
    disable_ssl_verify: bool = False,
    follow_redirects: bool = False,
) -> dict[str, Any]:
    """Perform an HTTP request based on the user choice."""
    start_time: datetime = datetime.now()
    CHOICE: str = method.upper()
    with Client(
        verify=not disable_ssl_verify,
        follow_redirects=follow_redirects,
    ) as client:
        match CHOICE:
            case HTTPMethod.GET.value:
                response: Response = client.get(
                    url,
                    headers=json.loads(headers) if headers else headers,
                )
            case HTTPMethod.POST.value:
                response: Response = client.post(
                    url,
                    json=json.loads(payload),
                    headers=json.loads(headers) if headers else headers,
                )
            case HTTPMethod.PUT.value:
                response: Response = client.put(
                    url,
                    json=json.loads(payload),
                    headers=json.loads(headers) if headers else headers,
                )
            case HTTPMethod.PATCH.value:
                response: Response = client.patch(
                    url,
                    json=json.loads(payload),
                    headers=json.loads(headers) if headers else headers,
                )
            case HTTPMethod.DELETE.value:
                response: Response = client.delete(
                    url,
                    headers=json.loads(headers) if headers else headers,
                )
            case _:
                raise ValueError(f"Unsupported HTTP method: {method}")
    end_time: datetime = datetime.now()
    response_time: timedelta = end_time - start_time
    return {"response": response, "response_time": response_time}


def print_response_info(response: Response, response_time: timedelta) -> None:
    """Pretty print the response information."""
    console.rule("[bold]Response Information[/bold]", style="blue", align="center")

    table = Table(box=box.SQUARE)
    table.add_column("Field", style="cyan", justify="right")
    table.add_column("Value", justify="left")

    table.add_row("Status Code:", str(response.status_code))
    table.add_row("HTTP Method:", response.request.method)
    table.add_row("URL:", str(response.url))
    table.add_row("Response Time:", str(response_time))

    console.print(table)


def print_response_headers(response: Response) -> None:
    """Pretty print the response headers information."""
    console.rule("[bold]Response Headers[/bold]", style="blue", align="center")

    table = Table(box=box.SQUARE)
    table.add_column("Header", style="cyan", justify="right")
    table.add_column("Value", justify="left")

    for name, value in response.headers.items():
        table.add_row(f"{name}:", value)

    console.print(table)


def print_response_body(response: Response) -> None:
    """Pretty print the response body information."""
    console.rule("[bold]Response Body[/bold]", style="blue", align="center")
    try:
        body = json.loads(response.text)
        formatted_body: str = json.dumps(body, indent=4)
        console.print(formatted_body)
    except json.JSONDecodeError:
        console.print(response.text)


def print_full_response(response: Response, response_time: timedelta) -> None:
    """Composition of all pretty print helper utils functions."""
    print_response_info(response, response_time)
    print_response_headers(response)
    print_response_body(response)
