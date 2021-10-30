# Question: Easy
'''
At a lemonade stand, each lemonade costs $5.

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.
'''
from typing import List
from collections import Counter
import logging


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance = Counter()
        if bills[0] != 5:
            return False
        for value in bills:
            value = str(value)
            if value == '5':
                balance.update(value)
            elif value == '10':
                balance.update('1')
                balance.subtract('5')
            else:
                if balance['1'] < 1:
                    balance.subtract('5')
                    balance.subtract('5')
                else:
                    balance.subtract('1')
                balance.subtract('5')
            if balance['5'] < 0:
                return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
    bills = [5, 5, 5, 10, 20]
    bills2 = [5, 5, 10]
    bills3 = [5, 5, 10, 10, 20]
    result = Solution()
    logging.info(f'Able to return : {result.lemonadeChange(bills2)}')
