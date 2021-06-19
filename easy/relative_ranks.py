#Question: Easy
'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
'''
from typing import List
import logging


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sorted_num = sorted(nums, reverse=True)
        ans = []
        for value in nums:
            rank = sorted_num.index(value)
            if not rank:
                ans.append('Gold Medal')
            elif rank == 1:
                ans.append('Silver Medal')
            elif rank == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(rank+1))
        return ans


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    nums = [5, 4, 3, 2, 1]
    logging.info(f'{result.findRelativeRanks(nums)}')

