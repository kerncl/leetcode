#Question: easy
#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#You may return any answer array that satisfies this condition.
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        sort_list = ['']*len(A)
        i = 1
        j = 0
        for value in A:
            if value % 2 == 0:
                sort_list[j]=value
                j += 1
            else:
                sort_list[len(A)-i] = value
                i +=1
        return sort_list


A = [3, 1, 2, 4]
result = Solution()
sort_list = result.sortArrayByParity(A)
print('Sorted value:', sort_list)
