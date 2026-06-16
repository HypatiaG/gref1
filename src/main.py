import typer
from commands import calendar, session, race

app = typer.Typer(help="FastF1 CLI")

app.add_typer(session.app, name="session")
app.add_typer(calendar.app, name="calendar")
app.add_typer(race.app, name="race")

if __name__ == "__main__":
    app()