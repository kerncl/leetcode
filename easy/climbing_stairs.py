#Question: Easy
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
import logging
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        ones = n
        twos = 0
        summ = 0

        while ones >= 0:
            summ += self.calculate_combinations(ones, twos)

            ones -= 2
            twos += 1
        return int(summ)


    def calculate_combinations(self, one, two):
        total = one + two
        total = math.factorial(int(total))
        one = math.factorial(int(one))

        two = math.factorial(int(two))

        den = one * two
        answer = total / den
        return answer

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [1, 2] + [0] * (n - 2)

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    n = 3
    result = Solution()
    result2 = Solution2()
    logging.info(f'Number of step needed: {result2.climbStairs(n)}')