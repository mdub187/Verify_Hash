import hashlib
import typer
from rich import print

app = typer.Typer()

@app.command()
def verify(
    filepath: str = typer.Argument(..., help="Path to the file to verify"),
    expected: str = typer.Option(
        ..., "--checksum", "-c", help="Expected SHA-256 checksum"
    ),
):
    """Compute SHA-256 of FILEPATH and compare to EXPECTED."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)

    result = h.hexdigest()
    if result == expected.lower():
        print(f":white_check_mark: [green]File OK![/]")
    else:
        print(f":x: [red]Checksum mismatch![/] Expected {expected}, got {result}")

if __name__ == "__main__":
    app()
