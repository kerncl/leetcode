"""
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.
"""
import logging
import sys


class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        N = n//2
        r = 2
        if n%2:
            # odd
            result = N/2*(2*2+(N-1)*r)
            pass
        else:
            # even
            result = N/2*(2+(N-1)*r)
            pass

        return result


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [(3, 2),
                    (6, 9)]

    for n, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.minOperations(n)
        assert myresult == expected_result, log.error(f'Expected Result {expected_result}, but received {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)