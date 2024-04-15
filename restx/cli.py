import typer
from rich.console import Console

from restx.utils import (
    crud_manager,
    print_full_response as pretty_print_response,
)


app = typer.Typer()
console = Console()


@app.command()
def get(
    url: str,
    headers: str = typer.Option(None, "--header", "-H", help="Custom headers"),
    disable_ssl_verify: bool = typer.Option(
        False, "--disable-ssl-verify", help="Disable SSL certificate verification"
    ),
    follow_redirects: bool = typer.Option(
        False, "--follow-redirects", help="Follow HTTP redirects"
    ),
) -> None:
    """Send a GET request."""
    response, response_time = crud_manager(
        url=url,
        method="GET",
        headers=headers,
        disable_ssl_verify=disable_ssl_verify,
        follow_redirects=follow_redirects,
    ).values()
    pretty_print_response(response, response_time)


@app.command()
def post(
    url: str,
    payload: str = typer.Option(..., "--payload", "-p", help="Payload data"),
    headers: str = typer.Option(None, "--header", "-H", help="Custom headers"),
    disable_ssl_verify: bool = typer.Option(
        False, "--disable-ssl-verify", help="Disable SSL certificate verification"
    ),
    follow_redirects: bool = typer.Option(
        False, "--follow-redirects", help="Follow HTTP redirects"
    ),
) -> None:
    """Send a POST request."""
    response, response_time = crud_manager(
        url=url,
        method="POST",
        payload=payload,
        headers=headers,
        disable_ssl_verify=disable_ssl_verify,
        follow_redirects=follow_redirects,
    ).values()
    pretty_print_response(response, response_time)


@app.command()
def put(
    url: str,
    payload: str = typer.Option(..., "--payload", "-p", help="Payload data"),
    headers: str = typer.Option(None, "--header", "-H", help="Custom headers"),
    disable_ssl_verify: bool = typer.Option(
        False, "--disable-ssl-verify", help="Disable SSL certificate verification"
    ),
    follow_redirects: bool = typer.Option(
        False, "--follow-redirects", help="Follow HTTP redirects"
    ),
) -> None:
    """Send a PUT request."""
    response, response_time = crud_manager(
        url=url,
        method="PUT",
        payload=payload,
        headers=headers,
        disable_ssl_verify=disable_ssl_verify,
        follow_redirects=follow_redirects,
    ).values()
    pretty_print_response(response, response_time)


@app.command()
def patch(
    url: str,
    payload: str = typer.Option(..., "--payload", "-p", help="Payload data"),
    headers: str = typer.Option(None, "--header", "-H", help="Custom headers"),
    disable_ssl_verify: bool = typer.Option(
        False, "--disable-ssl-verify", help="Disable SSL certificate verification"
    ),
    follow_redirects: bool = typer.Option(
        False, "--follow-redirects", help="Follow HTTP redirects"
    ),
) -> None:
    """Send a PATCH request."""
    response, response_time = crud_manager(
        url=url,
        method="PATCH",
        payload=payload,
        headers=headers,
        disable_ssl_verify=disable_ssl_verify,
        follow_redirects=follow_redirects,
    ).values()
    pretty_print_response(response, response_time)


@app.command()
def delete(
    url: str,
    headers: str = typer.Option(None, "--header", "-H", help="Custom headers"),
    disable_ssl_verify: bool = typer.Option(
        False, "--disable-ssl-verify", help="Disable SSL certificate verification"
    ),
    follow_redirects: bool = typer.Option(
        False, "--follow-redirects", help="Follow HTTP redirects"
    ),
) -> None:
    """Send a DELETE request."""
    response, response_time = crud_manager(
        url=url,
        method="DELETE",
        headers=headers,
        disable_ssl_verify=disable_ssl_verify,
        follow_redirects=follow_redirects,
    ).values()
    pretty_print_response(response, response_time)


if __name__ == "__main__":
    app()
