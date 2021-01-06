#Question: Easy
'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''
from typing import List
import logging

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(digit) for digit in digits])
        num_list = list(str(int(num) + 1))
        if len(num_list) < len(digits):
            for _ in range(len(digits)-len(num_list)):
                num_list.insert(0, 0)
        return num_list
        # for i in range(1, len(digits)+1):
        #     if str(digits[-i]).isdigit():
        #         if digits[-i] == 9:
        #             digits.insert(-i, 1)
        #             digits[-i] = 0
        #         else:
        #             digits[-i] += 1
        #         return digits


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    digits = [4, 3, 2, 1]
    digits2 = [9]
    digits3 = [0,0,0]
    logging.info(f'{result.plusOne(digits3)}')