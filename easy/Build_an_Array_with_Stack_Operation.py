#Question: Easy
'''
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.
Build the target array using the following operations:
Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.
Return the operations to build the target array.
You are guaranteed that the answer is unique.
'''
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        for index in range(1, n+1):
            if index in target:
                output.append('Push')
            else:
                output.extend(['Push', "Pop"])
            if index == target[len(target)-1]:
                return output

class Solution2:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return [ 'Push' if index in target else [''].extend(['Push','Pop']) for index in range(1, n+1)]


class Solution3:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        for i in range(1,target[-1]+1):
            output.append('Push')
            if i not in target:
                output.append('Pop')

        return output


result = Solution()
target = [1, 3]
n = 3
result = Solution()
print(f'Operation: {result.buildArray(target, n)}')
result2 = Solution2()
print(f'Operation: {result2.buildArray(target, n)}')
result3 = Solution3()
print(f'Operation: {result3.buildArray(target, n)}')