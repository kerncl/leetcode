#Question: Easy
'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
'''
from datetime import datetime
import logging


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = date1.split('-')
        y2, m2, d2 = date2.split('-')
        date1 = datetime.now().replace(year=int(y1), month=int(m1), day=int(d1))
        date2 = datetime.now().replace(year=int(y2), month=int(m2), day=int(d2))
        diff = date2 - date1
        return abs(diff.days)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    date1 = "2019-06-29"
    date2 = "2019-06-30"
    logging.info(f'Date difference: {result.daysBetweenDates(date1, date2)}')