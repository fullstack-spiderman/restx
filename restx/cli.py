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


if __name__ == "__main__":
    app()
