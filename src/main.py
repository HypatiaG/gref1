import typer
from commands import calendar, session

app = typer.Typer(help="FastF1 CLI — Formula 1 data at your fingertips")

app.add_typer(session.app, name="session")
app.add_typer(calendar.app, name="calendar")

if __name__ == "__main__":
    app()