#Question: Easy
'''
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.
'''
import logging


class Solution:
    def binaryGap(self, n: int) -> int:
        n_bin = bin(n)
        if not n_bin.count('1'):
            return 0
        diff = 0
        for index, value in enumerate(n_bin[2:]):
            if value == '1':
                if not index:
                    temp_index = index
                elif diff < (index - temp_index):
                    diff = index - temp_index
                temp_index = index
        return diff


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    n = 22
    n2 = 6
    n3 = 8
    n4 = 1
    logging.info(f'The maximum number between bit to bit: {result.binaryGap(n4)}')