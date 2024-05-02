from datetime import datetime


class Record:
    def __init__(self, record_id: int | None, habit_id: int, date: str, done: str = "True"):
        self.id = record_id
        self.habit_id = habit_id
        self.date = datetime.fromisoformat(date)
        self.done = bool(done)
