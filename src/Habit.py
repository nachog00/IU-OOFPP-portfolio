import datetime

PERIODICITIES = {
    "d": {
        "name": "Daily",
        "duration": datetime.timedelta(days=1),
    },
    "w": {
        "name": "Weekly",
        "duration": datetime.timedelta(weeks=1),
    },
    "m": {
        "name": "Monthly",
        "duration": datetime.timedelta(weeks=4),
    },
    "y": {
        "name": "Yearly",
        "duration": datetime.timedelta(weeks=52),
    },
}


class Habit:
    def __init__(
            self,
            id: int | None,
            title: str,
            description: str,
            periodicity_id: str,
            start_date: str | datetime.date
    ):
        self.id = id
        self.title = title
        self.description = description
        self.periodicity_id = periodicity_id
        self.start_date = datetime.date.fromisoformat(start_date) if type(start_date) is str else start_date

    @property
    def periodicity(self):
        return PERIODICITIES[self.periodicity_id]
