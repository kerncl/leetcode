# Question: Easy
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
from typing import List
import logging


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Time exceded
        # max_profit = 0
        # for day,price in enumerate(prices):
        #     for continue_day in range(day, len(prices)):
        #         profit = prices[continue_day] - price
        #         if profit > max_profit:
        #             max_profit = profit
        # return max_profit

        if not prices:
            return 0

        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            if maxprofit < price - minprice:
                maxprofit = price - minprice
        return maxprofit




if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 5, 4, 3, 1]
    prices3 = [1]
    prices4 = [2, 4, 1]
    logging.info(f'Maximum Profit : {result.maxProfit(prices4)}')
