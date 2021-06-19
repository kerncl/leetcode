# Question: Easy
'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''
import logging


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def check_status(low:int, high: int) -> int:
            """
            Check odd or even number, return 1 if odd else 0
            Args:
                value (int):

            Returns:
                bool: return 1 is odd else 0
            """
            if low % 2:
                if high % 2:
                    return 1
            return 0

        length = high - low

        return (length+1) // 2 + check_status(low, high)

        #return sum(1 for num in range(low, high+1) if num % 2)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
    result = Solution()
    low = 3
    high = 7
    low2= 798273637
    high2 = 970699661
    low3 = 21
    high3 = 22
    logging.info(f'Number of Odd: {result.countOdds(low2, high2)}')
