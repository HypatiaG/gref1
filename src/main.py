import typer
from commands import session

app = typer.Typer(help="FastF1 CLI — Formula 1 data at your fingertips")

app.add_typer(session.app, name="session")

if __name__ == "__main__":
    app()