import sqlite3
from src.Habit import Habit
from src.Record import Record


class Db:
    def __init__(self, db_file="data/default.data", debug: bool = False):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.debug = debug

    def create_tables(self):
        """
        Creates both habits and records tables if they do not exist already
        :return:
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                periodicity_id TEXT,
                start_date TEXT
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY,
                habit_id INTEGER NOT NULL,
                date TEXT,
                done INTEGER,
                FOREIGN KEY (habit_id) REFERENCES habits(id)
            )
            """
        )
        self.conn.commit()

    def reset(self):
        self.cursor.execute("DROP TABLE IF EXISTS habits")
        self.cursor.execute("DROP TABLE IF EXISTS records")
        self.create_tables()

    def insert_habit(self, habit: Habit):
        self.cursor.execute(
            """
            INSERT INTO habits (title, description, periodicity_id, start_date)
            VALUES (?, ?, ?, ?)
            """,
            (habit.title, habit.description, habit.periodicity_id, habit.start_date),
        )
        self.conn.commit()

    def get_habits(self, periodicity_id: str | None) -> list[Habit]:
        habits = []
        if periodicity_id is not None:
            self.cursor.execute("SELECT * FROM habits WHERE periodicity_id = ?", periodicity_id)
        else:
            self.cursor.execute("SELECT * FROM habits")
        for habit in self.cursor.fetchall():
            habits.append(
                Habit(
                    habit[0],
                    habit[1],
                    habit[2],
                    habit[3],
                    habit[4],
                )
            )
        return habits

    def insert_record(self, record: Record):
        self.cursor.execute(
            """
            INSERT INTO records (habit_id, date, done)
            VALUES (?, ?, ?)
            """,
            (record.habit_id, record.date, record.done),
        )
        self.conn.commit()

    def get_records_for_habit(self, habit_id) -> list[Record]:
        records = []
        self.cursor.execute("SELECT * FROM records WHERE habit_id = ?", (habit_id,))
        for record in self.cursor.fetchall():
            records.append(
                {
                    "record_id": record[0],
                    "habit_id": record[1],
                    "date": record[2],
                    "done": record[3],
                }
            )
        return [Record(**record) for record in records]
