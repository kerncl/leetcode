"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""
import math


def solution(v):
    max_iter = math.floor(math.sqrt(v))
    factors = []
    for i in range(1, max_iter + 1):
        if not v % i:
            factors.append(i)

    if math.ceil(math.pow(max_iter,2)) == v:
        return len(factors) * 2 -1
    return len(factors)*2


if __name__ == '__main__':
    n = 17
    print(f'{n} has {solution(n)} factor')
