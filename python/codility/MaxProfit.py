"""An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
"""
import math

def merge(l,r):
    if not len(l):
        return r

    if not len(r):
        return l

    r_i = l_i = 0
    result = []
    while len(result) < len(l) + len(r):
        if l[l_i] <= r[r_i]:
            result.append(l[l_i])
            l_i +=1
        else:
            result.append(r[r_i])
            r_i +=1

        if len(l) == l_i:
            result.extend(r[r_i:])
            break

        if len(r) == r_i:
            result.extend(l[l_i:])
            break
    return result

def merge_sort(a):
    if len(a)<2:
        return a
    mid = len(a)//2

    return merge(merge_sort(a[mid:]), merge_sort(a[:mid]))

def solution(a):
    max_v = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] > a[i]:
                diff = a[j] - a[i]
                if diff > max_v: max_v =diff
    return max_v


def solution2(a):
    min_v = a[0]
    max_diff = a[1] - a[0]
    for i in range(2,len(a)):
        current_diff = a[i] - a[i-1]
        max_diff = max(max_diff, a[i]-min_v, current_diff)
        if max_diff == current_diff:
            min_v = a[i-1]

    return max_diff

if __name__ == '__main__':
    a = [23171, 21011, 21123, 21366, 21013, 21367]
    print(f'Max profit {a}: {solution(a)}')
    print(f'Max profit {a}: {solution2(a)}')
