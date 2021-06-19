#Question: Easy
'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
'''
from typing import List
import logging


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for account in accounts:
            total = sum(account)
            maximum = max(total, maximum)
        return maximum

class Solution2:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    result2 = Solution2()
    accounts = [[1, 2, 3], [3, 2, 1]]
    logging.info(f'Richest Customer Wealth: {result2.maximumWealth(accounts)}')