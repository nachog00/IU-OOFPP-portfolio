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
            start_date: str | datetime.date,
            db
    ):
        self.id = id
        self.title = title
        self.description = description
        self.periodicity_id = periodicity_id
        self.start_date = datetime.date.fromisoformat(start_date) if type(start_date) is str else start_date
        self.db = db

    @property
    def periodicity(self):
        return PERIODICITIES[self.periodicity_id]

    @property
    def records(self):
        return self.db.get_records_for_habit(self.id)


    def is_latest_period_done(self, current_date: datetime.date = None):
        """
        Determines if the habit is done on the latest period (or on the period corresponding to the current date)
        :param current_date:
        :return:
        """
        records = self.records
        current_date = current_date if current_date is not None else datetime.date.today()
        # decide the period for the current date, return True if any record already done within that period
        return self.is_period_done_for_date(current_date)

    def get_period_for_date(self,date: datetime.date):
        records = self.records
        [d1,d2] = [ self.start_date , self.start_date + self.periodicity["duration"]]
        if date < d1:
            return None
        while date >= d2:
            [d1,d2] = [d2,d2 + self.periodicity["duration"]]
        return [d1,d2]

    def is_period_done(self, period: list[datetime.date]):
        records = self.records
        return any([period[0] <= record.date.date() < period[1] for record in records])

    def is_period_done_for_date(self, date: datetime.date):
        period = self.get_period_for_date(date)
        return self.is_period_done(period) if period is not None else False

    @property
    def summary(self, today: datetime.date = None):
        summary = {
            "periods_total": 0,
            "missed": 0,
            "done": 0,
            "best_streak": 0,
            "current_streak": 0,
            "percentage": 0
        }
        records = self.records
        today = today if today is not None else datetime.date.today()
        period = self.periodicity["duration"]
        start_date = self.start_date
        [d1, d2, r] = [start_date, start_date + period, []]
        while d1 <= today:
            # 
            summary["periods_total"] += 1

            r = [records for record in records if d1 <= record.date.date() < d2]

            if len(r) > 0:
                summary["done"] += 1
                summary["current_streak"] += 1
                if summary["current_streak"] > summary["best_streak"]:
                    summary["best_streak"] = summary["current_streak"]
            else:
                summary["missed"] += 1
                summary["current_streak"] = 0

            [d1, d2, r] = [d2, d2 + period, []]

        summary["percentage"] = summary["done"] / summary["periods_total"] if summary["periods_total"] > 0 else 0

        return summary
