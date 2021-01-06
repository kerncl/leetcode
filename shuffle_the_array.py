#Question: (Easy)
#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n+i])
        return output


number = [1, 1, 2, 2]
result = Solution()   # result is an object
print(result.shuffle(nums=number, n=2))


