#Question: easy
#Given an array of characters, compress it in-place.
#The length after compression must always be smaller than or equal to the original array.
#Every element of the array should be a character (not int) of length 1.
#After you are done modifying the input array in-place, return the new length of the array.
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        sort_input = list(set(chars))
        compress_list = []
        for index in sort_input:
            if chars.count(index) == 1:
                compress_list.append(index)
            else:
                compress_list.extend([index, chars.count(index)])
        return compress_list


input = ["a", "a", "b", "b", "c", "c", "c"]
result = Solution()
compress_list = result.compress(input)
print('Compress list:', compress_list)