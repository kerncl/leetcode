"""
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
"""
from collections import Counter
import math

def solution(a):
    counter = 0
    i_header = 0
    i_tail = len(a) - 1
    while i_header <= i_tail:
        head = abs(a[i_header])
        tail = abs(a[i_tail])
        print(f"head{i_header}: {head}, tail{i_tail}: {tail}")
        if head == tail:
            i_tail -= 1
            continue
        if head >  tail:
            print(f"COUNTER +1")
            i_header += 1
            counter += 1
        else:
            print(f"COUNTER +1")
            i_tail -= 1
            counter += 1
    else:
        counter += 1 # last element
    return counter

if __name__ == '__main__':
    a = [-5,-3, -1, 0, 3, 6]
    b = [-6, -5,-3, -1, 0 ,3, 6, 7]
    print(solution(b))
