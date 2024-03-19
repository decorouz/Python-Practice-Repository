"""A function to plot chores during a week using Enum"""
from typing import Dict
from enum import Flag


class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64


# Lets get some chores setup

chores_for_may = {
    "feed the cat": Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
    "take out the trash": Weekday.TUESDAY | Weekday.SUNDAY,
    "take twins to movies": Weekday.FRIDAY | Weekday.SUNDAY,
}


def show_chores(chores: Dict[str, Weekday], day: Weekday) -> None:
    """Display the chores for a given day"""
    for chore, days in chores.items():
        if day in days:
            print(chore)


show_chores(chores_for_may, Weekday.SUNDAY)
