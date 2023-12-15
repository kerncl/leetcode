"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
"""

import logging

def in_between(x1, x2, y1, y2):
    # pattern 1
    # -5 < x < 10
    # -1 < x < 3
    # pattern 2
    # -5 < x < 10
    # -2 < y < 15
    if (x1 <= y1 and y1 <= x2) or (y1 <= x1 and x1 <= y2):
        return True


def solution(a):
    circles = {}
    for i, radius in enumerate(a):
        circles[i] = {
            'x1': i - radius,
            'x2': i + radius,
        }

    print(f'Cirlcle: {circles}')
    pairs = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if in_between(*circles[i].values(), *circles[j].values()):
                pairs.append((i,j))

    print(f'Total : {len(pairs)}')
    return pairs

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    a = [1,5,2,1,4,0]
    logging.info(f'{a} had {solution(a)} intercept')
