from rich.console import Console
import fastf1
from commands import session

console = Console()

def load_session(year, round, session_type):
    session = fastf1.get_session(year, round, session_type)
    with console.status("[bold green]Loading session..."):
        session.load()
        return session