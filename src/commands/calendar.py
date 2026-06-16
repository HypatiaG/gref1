import fastf1 as f1
import logging
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()
logging.getLogger("fastf1").setLevel(logging.CRITICAL)

@app.command(help="Display race schedule in a year")
def schedule(
    year: int = typer.Option(...,"--year","-y", help="Year of the session")):

    session = f1.get_event_schedule(year)
    table = Table(
        title=f"{year} — Race Schedule",
        show_lines=True,
        header_style="bold magenta",
    )

    table.add_column("Round", justify="center", style="cyan", no_wrap=True)
    table.add_column("Country", style="white")
    table.add_column("Location", justify="right", style="yellow")
    table.add_column("OfficialEventName", justify="right", style="yellow")
    table.add_column("EventDate", justify="right", style="yellow")


    for _, row in session.iterrows():
        table.add_row(
            str(int(row["RoundNumber"])),
            str(row["Country"]),
            str(row["Location"]),
            str(row["OfficialEventName"]),
            row["EventDate"].date().isoformat()
        )

    console.print(table)