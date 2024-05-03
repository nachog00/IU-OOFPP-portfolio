from datetime import datetime
import rich
from rich.table import Table

from src.Habit import Habit, PERIODICITIES
from src.Record import Record
from src.Db import Db
from src.analytics import analytics


class App:
    def __init__(self, console, debug: bool = False, database_file: str = None):
        self.debug = debug
        self.console = console
        self.db = Db(db_file=database_file)
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
        habit = Habit(None, title, description, periodicity, start_date, self.db)
        self.db.insert_habit(habit)
        self.console.print("💾", f"[bold magenta]Stored habit: {title}[/bold magenta]")

    def mark_done(self, habit_id: int):
        self.db.insert_record(Record(record_id=None, habit_id=habit_id, date=self.current_date.isoformat()))

    def get_habits(self, periodicity_id: str | None) -> list[Habit]:
        return self.db.get_habits(periodicity_id)

    def list_habits(self, periodicity: str | None):
        habits = self.get_habits(periodicity)

        #  ---------- Data table ----------
        # title
        periodicity_title = PERIODICITIES[periodicity]["name"] if periodicity is not None else "All"
        self.console.print("📃", f"[bold magenta] {periodicity_title} habits ({len(habits)}) [/bold magenta]")

        # build the table
        table = Table(show_header=True, header_style="bold blue")

        # build the columns
        table.add_column("#", style="dim", width=3)
        table.add_column("Title", min_width=15)
        table.add_column("Description", min_width=30)
        table.add_column("Periodicity", min_width=10)
        table.add_column("Start Date", min_width=10)
        table.add_column("# Periods", min_width=5)
        table.add_column("Current streak", min_width=5)
        table.add_column("Best streak", min_width=5)
        table.add_column("% Done", min_width=5)

        # add rows to the table
        for idx, habit in enumerate(habits):
            summary = habit.summary
            table.add_row(
                str(idx).rjust(3),
                habit.title,
                habit.description,
                habit.periodicity["name"],
                habit.start_date.strftime("%d/%m/%Y"),
                str(summary["periods_total"]),
                str(summary["current_streak"]),
                str(summary["best_streak"]),
                "{:.0f}%".format(summary["percentage"] * 100).rjust(5),
            )

        # print the table
        self.console.print(table)

    def analytics(self):

        self.console.print("[bold magenta]Analytics[/bold magenta]")
        
        data = analytics(self)

        for key, value in data.items():

            table = Table(title=str(key), show_header=True, header_style="bold blue")

            table.add_column("Periodicity", min_width=10)
            table.add_column("Value", min_width=10)
            table.add_column("Habit", min_width=10)

            for p, h in value.items():

                if h == None:
                    continue

                periodicity = PERIODICITIES[p]["name"] if p != "a" else "All"

                table.add_row( periodicity , str(h["value"]), h["habit"].title)

            self.console.print(table)
        


    def launch(self):
        ...
