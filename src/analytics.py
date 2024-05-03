from datetime import date
from typing import Dict, Any

from rich.pretty import pprint

from src.App import App

from src.Habit import PERIODICITIES, Habit

from rich.console import Console


def analytics(app: App):
    """
    this function recopilates key app wide statistics including
        * longest overall streak
        * longest current streak
        * highest percentage of completion
        * oldest habit
    All of them, overall and by periodicity are calculated
    :param app:
    :return:
    """
    methods = {
        "longest_streak": get_longest_streak,
        "longest_current_streak": get_longest_current_streak,
        "highest_percentage_of_completion": get_highest_percentage_of_completion,
        "oldest_habit": get_oldest_habit,
    }

    analytics_result = {}

    habits = app.get_habits(periodicity_id=None)
    habits_by_per = {"a": []}
    for p in PERIODICITIES:
        habits_by_per[p]= []

    for hbp in habits_by_per:
        habits_by_per[hbp] = [h for h in habits if h.periodicity_id == hbp or hbp == "a"]

    for x in methods:
        method = methods[x]
        analytics_result[x] = {}
        for hbp in habits_by_per:
            habits = habits_by_per[hbp]
            analytics_result[x][hbp] = method(habits) if len(habits) > 0 else None

    return analytics_result


def get_longest_x(habits: list[Habit], x: str) -> dict[str, Habit | int]:
    result = habits[0]
    for habit in habits[1:]:
        if habit.summary[x] > result.summary[x]:
            result = habit
    return {
        "habit": result,
        "value": result.summary[x]
    }


def get_longest_streak(habits: list[Habit]) -> Habit:
    return get_longest_x(habits, "best_streak")


def get_longest_current_streak(habits: list[Habit]) -> Habit:
    return get_longest_x(habits, "current_streak")


def get_highest_percentage_of_completion(habits: list[Habit]) -> Habit:
    return get_longest_x(habits, "percentage")


def get_oldest_habit(habits: list[Habit]) -> dict[str, Habit | Any]:
    result = habits[0]
    for habit in habits[1:]:
        if habit.start_date < result.start_date:
            result = habit
    return {
        "habit": result,
        "value": result.start_date
    }


if __name__ == "__main__":
    app = App(Console(), database_file='../data/default.db')
    result = analytics(app)
    pprint(result)
