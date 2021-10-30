# Question: Easy
'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
'''
from typing import List
import logging


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        result = []
        for index,num in enumerate(arr):
            if not num:
                result.append(0)
            result.append(num)
            if len(result) >= length:
                break
        for i in range(length):
            arr[i]=result[i]



if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    result.duplicateZeros(arr)
