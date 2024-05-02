import datetime

import rich
import typer

from src.app import App

typer_app = typer.Typer()
console = rich.console.Console()


@typer_app.command(help="Add a new habit")
def new(title: str, description: str, periodicity: str = None, start_date: str = None):
    """
    Add a new habit
    :param title:
    :param description:
    :param start_date:
    :param periodicity:
    :return:
    """
    app = App(console=console, debug=False)
    app.add_habit(title=title, description=description, start_date=start_date, periodicity=periodicity)


@typer_app.command(help="Mark habit as done")
def mark_done(habit_id: int, current_date: str):
    """
    Mark habit as done
    :param habit_id:
    :param current_date:
    :return:
    """
    typer.echo(f"Completed habit {habit_id}")
    pass


@typer_app.command(help="See habits list")
def habits(periodicity: str = "d", start_date: str = None, end_date: str = None):
    """
    List all habits
    :param periodicity:
    :param start_date:
    :param end_date:
    :return:
    """
    typer.echo(f"Showing all {periodicity} habits between {start_date} and {end_date}")
    pass


@typer_app.command(help="Show app-wide analytics")
def analytics():
    """
    Shows app-wide analytics
    :return: None
    """
    typer.echo("Analytics")
    pass


@typer_app.command(help="Launch interactive loop")
def launch(debug: bool = False, current_date: str = None):
    typer.echo("Launching")
    pass
