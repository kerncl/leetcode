#Question: Easy
'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
'''
import logging
import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split('-')
        begin = datetime.date(int(year),1,1)
        end = datetime.date(int(year),int(month),int(day))
        return end.toordinal() - begin.toordinal()+1


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    date = "2019-01-09"
    logging.info(f' Total Day: {result.dayOfYear(date)}')