"""
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
"""
import logging
import sys
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row = len(rowSum)
        col = len(colSum)
        result = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if min(rowSum[i], colSum[j]):
                    val = min(rowSum[i], colSum[j])
                    result[i][j] = val
                    rowSum[i] -= val
                    colSum[j] -= val
        return result


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)'

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)

    log.addHandler(stream)

    test_pattern = [([3, 8], [4, 7],
                     [[3, 0],
                      [1, 7]]),
                    ([5, 7, 10], [8, 6, 8],
                     [[0, 5, 0],
                      [6, 1, 0],
                      [2, 0, 8]]),
                    ([14, 9], [6, 9, 8],
                     [[0, 9, 5],
                      [6, 0, 3]]),
                    ([1, 0], [1],
                     [[1],
                      [0]]),
                    ([0], [0],
                     [[0]])]

    for rowSum, colSum, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.restoreMatrix(rowSum=rowSum.copy(), colSum=colSum.copy())
        # assert myresult == expected_result, log.error(f'Expected result: {expected_result}, but received: {myresult}')
        assert rowSum == [sum(row) for row in myresult], log.error(f'Invalid row sum')
        assert colSum == [sum(myresult[i][j] for i in range(len(myresult))) for j in range(len(myresult[0]))]

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
