# Question: Easy
'''
We have n chips, where the position of the ith chip is position[i].
We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:
position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.
'''
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        length = 0
        if len(position) == 1:
            return 0
        if len(position) == 2:
            return (position[1] - position[0]) % 2
        if len(position) > 2:
            odd = 0
            even = 0
            for value in position:
                if value % 2:
                    odd +=1
                else:
                    even +=1
            if odd > even:
                return even
            else:
                return odd


position = [6, 4, 7, 8, 2, 10, 2, 7, 9, 7]
result = Solution()
print(f'Cost: {result.minCostToMoveChips(position)}')
