#Question: Easy
"""
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.
"""
import logging


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        remainder = 0
        while True:
            temp_numBottles = numBottles
            numBottles = (remainder + numBottles) // numExchange
            total += numBottles
            remainder = temp_numBottles % numExchange
            if (numBottles+remainder) < numExchange:
                break
        return total


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    numBottles = 9
    numExchange = 3
    numBottles2 = 15
    numExchange2 = 4
    numBottles3 = 5
    numExchange3 =5
    numBottles4 = 2
    numExchange4 = 3
    numBottles5 = 15
    numExchange5 = 8
    result = Solution()
    logging.info(f'Amount of water drink: {result.numWaterBottles(numBottles2, numExchange2)}')