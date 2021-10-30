# Question: Easy
'''
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
'''
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        final_list = []
        for index in range(1,len(arr)):
            if index == 1:
                temp = abs(arr[index] - arr[index-1])
                final_list.append([arr[index - 1], arr[index]])
            elif temp > abs(arr[index] - arr[index-1]):
                temp = arr[index] - arr[index-1]
            if temp == abs(arr[index] - arr[index-1]) and index != 1:
                    if min([abs(pair[1]-pair[0]) for pair in final_list]) != temp:
                        final_list.clear()
                    final_list.append([arr[index - 1], arr[index]])

        return final_list

class Solution2:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        target = min(diff)
        final = [[arr[i], arr[i + 1]] for i, d in enumerate(diff) if d == target]
        return final

arr = [40,11,26,27,-20]
arr2 = [4,2,1,3]
result = Solution()
print(f'Abs difference {result.minimumAbsDifference(arr1)}')
result2 = Solution2()
print(f'Abs difference {result2.minimumAbsDifference(arr1)}')
