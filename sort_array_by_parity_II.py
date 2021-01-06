# Question: Easy
'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.
'''

from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_list = []
        even_list = []
        for temp in A:
            if temp % 2:
                even_list.append(temp)
            else:
                odd_list.append(temp)
        final_list = []
        for o, e in zip(odd_list, even_list):
            final_list.append(o)
            final_list.append(e)
        return final_list


class Solution2:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        out = [''] * len(A)
        i, j = 0, 1
        for value in A:
            if value % 2:
                out[j] = value
                j += 2
            else:
                out[i] = value
                i += 2
        return out


result = Solution()
A = [4, 2, 5, 7]
print(f'output: {result.sortArrayByParityII(A)}')
result2 = Solution2()
print(f'output: {result2.sortArrayByParityII(A)}')
