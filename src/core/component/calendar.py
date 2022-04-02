import datetime as dt
import calendar as cl

class Calendar:
    """
        Data structure representing a calendar
    """
    def __init__(self, year: int):
        self.Year: int = year
        self.DaysPerMonth: list = []
        for month in range(1, 13):
            self.DaysPerMonth.append(dt._days_in_month(self.Year, month))