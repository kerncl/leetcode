# Question: Easy
"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
from typing import List
import logging


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #price_diff = [prices[index] - prices[index-1] for index in range(1,len(prices))]
        #earn = sum(price for price in price_diff if price>0)
        earn = sum(prices[index] - prices[index-1] for index in range(1,len(prices)) if (prices[index] - prices[index-1]) > 0 )
        return earn


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    prices2 = [1, 2, 3, 4, 5]
    prices3 = [7, 6, 4, 3, 1]
    logging.info(f'Max profit earn: {result.maxProfit(prices)}')
