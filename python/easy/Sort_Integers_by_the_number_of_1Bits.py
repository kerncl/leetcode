#Question: Easy
'''
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
Return the sorted array.
'''

from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit = {}
        final_bit = []
        if 0 in arr:
            final_bit.append(0)
            arr.pop(0)
        for value in sorted(arr):
            bit.setdefault(value, []).append(str(bin(value)).count('1'))
        key_list = list(bit.keys())
        value_list = list(bit.values())
        for value in sorted(bit.values()):
            index = value_list.index(value)
            final_bit.append(key_list[index])
            if len(value_list[index]) > 1:
                for _ in range(len(value_list[index])-1):
                    final_bit.append(key_list[index])
            del key_list[index]
            del value_list[index]
        return final_bit

class Solution2:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))

arr = [10000, 10000]
result = Solution()
print(f'result: {result.sortByBits(arr)}')
result2 = Solution2()
print(f'result: {result2.sortByBits(arr)}')