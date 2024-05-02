from datetime import datetime


class Record:
    def __init__(self, record_id, habit_id, date, done):
        self.id = record_id
        self.habit_id = habit_id
        self.date = datetime.fromisoformat(date).date()
        self.done = bool(done)