import json
import typer
from httpx import Client, Response
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def get(url: str) -> None:
    """Send a GET request."""
    with Client() as client:
        response: Response = client.get(url)
    console.print(response.json(), style="bold green")


@app.command()
def post(
    url: str, payload: str = typer.Option(..., "--payload", "-p", help="Payload data")
) -> None:
    """Send a POST request."""
    with Client() as client:
        response: Response = client.post(url, json=json.loads(payload))
    console.print(response.json(), style="bold green")


@app.command()
def delete(url: str, headers: str = None) -> None:
    """Send a DELETE request."""
    with Client() as client:
        response: Response = client.delete(url)
    console.print(response.json(), style="bold green")


if __name__ == "__main__":
    app()
