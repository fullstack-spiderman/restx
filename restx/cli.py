import typer
from rich.console import Console

from restx.utils import crud_manager, print_additional_info, print_response_body


app = typer.Typer()
console = Console()


@app.command()
def get(url: str, headers: str = None) -> None:
    """Send a GET request."""
    response, response_time = crud_manager(
        url=url, method="GET", headers=headers
    ).values()
    print_additional_info(response, response_time)
    print_response_body(response)


@app.command()
def post(
    url: str, payload: str = typer.Option(..., "--payload", "-p", help="Payload data")
) -> None:
    """Send a POST request."""
    response, response_time = crud_manager(
        url=url, method="POST", payload=payload
    ).values()
    print_additional_info(response, response_time)
    print_response_body(response)


@app.command()
def put(
    url: str, payload: str = typer.Option(..., "--payload", "-p", help="Payload data")
) -> None:
    """Send a PUT request."""
    response, response_time = crud_manager(
        url=url, method="PUT", payload=payload
    ).values()
    print_additional_info(response, response_time)
    print_response_body(response)


@app.command()
def patch(
    url: str, payload: str = typer.Option(..., "--payload", "-p", help="Payload data")
) -> None:
    """Send a PATCH request."""
    response, response_time = crud_manager(
        url=url, method="PATCH", payload=payload
    ).values()
    print_additional_info(response, response_time)
    print_response_body(response)


@app.command()
def delete(url: str, headers: str = None) -> None:
    """Send a DELETE request."""
    response, response_time = crud_manager(
        url=url, method="DELETE", headers=headers
    ).values()
    print_additional_info(response, response_time)
    print_response_body(response)


if __name__ == "__main__":
    app()
