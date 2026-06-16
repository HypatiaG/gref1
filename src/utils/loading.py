from requests import session
from rich.console import Console
import fastf1 as f1


console = Console()

def load_session(year: int, round: int, session_type: str):
    session = f1.get_session(year, round, session_type)
    with console.status("[bold green]Loading session..."):
        session.load()
        return session
    
def load_season(year: int):
    with console.status("[bold magenta]Loading season..."):
        session = f1.get_event_schedule(year)
        return session