import datetime

import typer

app = typer.Typer()


@app.command(help="Add a new habit")
def new(title: str, description: str, start_date: str, periodicity: str):
    """
    Add a new habit
    :param title:
    :param description:
    :param start_date:
    :param periodicity:
    :return:
    """
    typer.echo("New habit")
    pass


@app.command(help="Mark habit as done")
def mark_done(habit_id: int, current_date: str):
    """
    Mark habit as done
    :param habit_id:
    :param current_date:
    :return:
    """
    typer.echo(f"Completed habit {habit_id}")
    pass


@app.command(help="See habits list")
def habits(periodicity: str, start_date: str, end_date: str):
    """
    List all habits
    :param periodicity:
    :param start_date:
    :param end_date:
    :return:
    """
    typer.echo(f"Showing all {periodicity} habits between {start_date} and {end_date}")
    pass


@app.command(help="Show app-wide analytics")
def analytics():
    """
    Shows app-wide analytics
    :return: None
    """
    typer.echo("Analytics")
    pass


@app.command(help="Launch interactive loop")
def launch(debug: bool = False, current_date: str = None):
    typer.echo("Launching")
    pass
