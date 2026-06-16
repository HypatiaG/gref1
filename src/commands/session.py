import logging
import pandas as pd
from rich.console import Console
from rich.table import Table
from utils.loading import load_session
import typer
import matplotlib.pyplot as plt
import pandas as pd
from timple.timedelta import strftimedelta
import fastf1
import fastf1.plotting
from fastf1.core import Laps

app = typer.Typer()
console = Console()
logging.getLogger("fastf1").setLevel(logging.CRITICAL)

def format_race_time(position, td):
    if pd.isna(td):
        return "No Time"

    if position == 1:
        return str(td).split(" days ")[-1][:-3]

    return f"+{td.total_seconds():.3f}"

@app.command(help="Display race results")
def race(
    year: int = typer.Option(...,"--year","-y", help="Year of the session"),
    round: int = typer.Option(...,"--round","-r", help="Round of the session")):

    session = load_session(year, round, "R")
    table = Table(
        title=f"{session.event['EventName']} {year} — Race Results",
        show_lines=True,
        header_style="bold magenta",
    )

    table.add_column("Pos", justify="center", style="cyan", no_wrap=True)
    table.add_column("Driver", style="white")
    table.add_column("Points", justify="right", style="yellow")
    table.add_column("Time", justify="right", style="yellow")


    for _, row in session.results.iterrows():
        table.add_row(
            str(int(row["Position"])),
            row["BroadcastName"],
            str(int(row["Points"])),
            format_race_time(
                int(row["Position"]),
                row["Time"]
            )
        )

    console.print(table)

@app.command(help="Display qualifying results")
def qualifying(
    year: int = typer.Option(...,"--year","-y", help="Year of the session"),
    round: int = typer.Option(...,"--round","-r", help="Round of the session")):

    fastf1.plotting.setup_mpl(mpl_timedelta_support=True, color_scheme=None)

    session = load_session(year, round, "Q")
    drivers = pd.unique(session.laps['Driver'])

    list_fastest_laps = list()
    for drv in drivers:
        drvs_fastest_lap = session.laps.pick_drivers(drv).pick_fastest()
        list_fastest_laps.append(drvs_fastest_lap)
    fastest_laps = Laps(list_fastest_laps) \
        .sort_values(by='LapTime') \
        .reset_index(drop=True)
    
    pole_lap = fastest_laps.pick_fastest()
    fastest_laps['LapTimeDelta'] = fastest_laps['LapTime'] - pole_lap['LapTime']


    table = Table(
        title=f"{session.event['EventName']} {year} — Qualifying Results",
        show_lines=True,
        header_style="bold magenta",
    )

    table.add_column("Driver", style="white")
    table.add_column("Lap Time", justify="right", style="yellow")
    table.add_column("Lap Time Delta", justify="right", style="yellow")


    for _, row in fastest_laps.iterrows():
        table.add_row(
            row["Driver"],
            row["LapTime"].__str__().split(" days ")[-1][:-3],
            row["LapTimeDelta"].__str__().split(" days ")[-1][:-3]
        )

    console.print(table)