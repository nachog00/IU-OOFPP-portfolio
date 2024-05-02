from datetime import datetime
import rich

from src.Habit import Habit
from src.db import Db


class App:
    def __init__(self, console: rich.console, debug: bool = False):
        self.debug = debug
        self.console = console
        self.db = Db()
        self.current_date = datetime.now().date()

    def add_habit(self, title: str, description: str, periodicity: str = None, start_date: str = None):
        """
        Adds habit to the database
        :param title:
        :param description:
        :param periodicity:
        :param start_date:
        :return:
        """
        periodicity = periodicity if periodicity is not None else "d"
        start_date = start_date if start_date is not None else self.current_date.isoformat()
        habit = Habit(None, title, description, periodicity, start_date)
        self.db.insert_habit(habit)
        self.console.print("💾", f"[bold magenta]Stored habit: {title}[/bold magenta]")

    def mark_done(self, habit_id: int):
        ...

    def get_habits(self, periodicity: str = "d", start_date: str = None, end_date: str = None):
        ...

    def get_analytics(self):
        ...

    def launch(self):
        ...
