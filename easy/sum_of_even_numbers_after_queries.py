#Question: Easy
'''
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
'''
from typing import List
import logging


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        final_list = []
        sum_even = sum(value for value in A if not value % 2)
        for value, index in queries:
            if not A[index] % 2:
                sum_even -= A[index]
            A[index] += value
            if not A[index] % 2:
                sum_even += A[index]
            final_list.append(sum_even)
        return final_list


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    logging.info(f'Final Output list {result.sumEvenAfterQueries(A, queries)}')