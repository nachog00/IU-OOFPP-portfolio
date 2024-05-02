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
            id: int,
            title: str,
            description: str,
            start_date: str,
            periodicity_id: str,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.periodicity_id = periodicity_id
        self.start_date = self.string_to_date(start_date)

    @staticmethod
    def string_to_date(date_string: str) -> datetime.date:
        """
        Parses a date string
        :param date_string:
        :return:
        """
        return datetime.datetime.strptime(date_string, "").date()
