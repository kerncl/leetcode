# Question: Easy
'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
'''
from typing import List
import logging
import itertools


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        time = set()
        temp = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
        binary_list = set()
        for value_list in itertools.combinations(temp, num):
            binary_list.add(sum(value_list))
        for binary in binary_list:
            time.add(self.convertBinarytoTime(binary))
        time = list(time - set(['']))
        return time

    def convertBinarytoTime(self, binary):
        if binary > 63:
            h = binary // 64
            m = binary % 64
        else:
            h = 0
            m = binary
        if h > 11 or m > 59:
            return ''
        return f'{h}:{"0"+str(m) if len(str(m))<2 else m }'


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    n = 8
    logging.info(f'Time: {result.readBinaryWatch(n)}')
