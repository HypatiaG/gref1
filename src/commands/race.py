import logging
import typer
from rich.console import Console
from rich.table import Table
from utils.loading import load_session

app = typer.Typer()
console = Console()
logging.getLogger("fastf1").setLevel(logging.CRITICAL)

@app.command(help="Display race stint of driver")
def stint(
    year: int = typer.Option(...,"--year","-y", help="Year of the season"),
    round: int = typer.Option(...,"--round","-r", help="Round in the season"),
    driver: str = typer.Option(...,"--driver","-d", help="Driver's code (e.g. HAM, VER, etc.)")):

    session = load_session(year, round, "R")
    laps = session.laps
    driver_name = session.get_driver(driver)["Abbreviation"]
    console.print(driver_name)

    stints = laps[["Driver", "Stint", "Compound", "LapNumber"]]
    stints = stints.groupby(["Driver", "Stint", "Compound"])
    stints = stints.count().reset_index()

    stints = stints.rename(columns={"LapNumber": "StintLength"})
    # console.print(stints[stints["Driver"] == driver_name])

    table = Table()
    table.add_column("Driver", justify="center", style="cyan", no_wrap=True)
    table.add_column("Stint", style="white")
    table.add_column("Compound", justify="right", style="yellow")
    table.add_column("StintLength", justify="right", style="yellow")

    for _, row in stints[stints["Driver"] == driver_name].iterrows():
        table.add_row(
            str(row["Driver"]),
            str(row["Stint"]),
            str(row["Compound"]),
            str(row["StintLength"])
        )

    console.print(table)

