#Question: Easy
'''
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.
'''
from typing import List
import logging


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        length = len(ops)
        max_num = 0
        for coor_x in range(m):
            for coor_y in range(n):
                count = 0
                for x,y in ops:
                    if coor_x < x and coor_y < y:
                        count += 1
                    else:
                        break
                if count == length:
                    max_num += 1
        return max_num

class Solution2:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x, y in ops:
            m = min(m, x)
            n = min(n, y)
        return m*n


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    result2 = Solution2()
    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    m2 = 39999
    n2 =39999
    ops2 = [[19999, 19999]]
    logging.info(f'maximum integer : {result2.maxCount(m, n, ops)}')