from datetime import datetime

from src.Habit import Habit
from src.db import Db

class App:
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.db = Db()
        self.current_date = datetime.now().date()

    def add_habit(self, habit: Habit):
        ...

    def mark_done(self, habit_id: int):
        ...

    def get_habits(self, periodicity: str = "d", start_date: str = None, end_date: str = None):
        ...

    def get_analytics(self):
        ...

    def launch(self):
        ...
