import datetime

import rich
import typer

from src.App import App

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
def mark_done(habit_id: int):
    """
    Mark habit as done
    :param habit_id:
    :return:
    """
    app = App(console=console, debug=False)
    app.mark_done(habit_id)


@typer_app.command(help="See habits list")
def habits(periodicity: str = None):
    """
    List all habits
    :param periodicity:
    :return:
    """
    app = App(console=console, debug=False)
    app.list_habits(periodicity)


@typer_app.command(help="Show app-wide analytics")
def analytics():
    """
    Shows app-wide analytics
    :return: None
    """
    app = App(console=console, debug=False)
    app.analytics()

@typer_app.command(help="Launch interactive loop")
def launch(debug: bool = False, current_date: str = None):
    typer.echo("Launching")
    pass
