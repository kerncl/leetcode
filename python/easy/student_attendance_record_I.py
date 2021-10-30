#Question: Easy
'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
'''
import logging
from collections import Counter


class Solution:
    def checkRecord(self, s: str) -> bool:
        count = Counter(s)
        if count['A'] > 1 or 'LLL' in s:
            return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    s = "PPALLP"
    s2 = 'PPALLL'
    logging.info(f'Good Student: {result.checkRecord(s2)}')