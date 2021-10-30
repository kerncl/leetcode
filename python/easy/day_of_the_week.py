#Questions: Easy
"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
"""
import calendar
import logging
from datetime import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return calendar.day_name[datetime.strptime(str(year)+'-'+str(month)+'-'+str(day), "%Y-%m-%d").date().weekday()]


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    day = 31
    month = 8
    year = 2019
    logging.info(f'Day: {result.dayOfTheWeek(day, month, year)}')