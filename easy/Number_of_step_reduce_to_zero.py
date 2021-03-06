#Question: easy
#Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2:
                num -= 1
            else:
                num = num / 2
            count += 1
        return count

num = 14
result = Solution()
Noiteration = result.numberOfSteps(num)
print('Number of iteration:', Noiteration)