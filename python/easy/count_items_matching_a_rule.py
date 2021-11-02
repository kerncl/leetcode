# Question: Easy
"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
"""

import logging
import sys
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        newitems = []
        counts = 0
        for item in items:
            newdict = {}
            for key, value in zip(('type','color', 'name'),item):
                newdict.update({key:value})
            newitems.append(newdict.copy())
        for newitem in newitems:
            if newitem[ruleKey] == ruleValue:
                counts+=1
        return counts


if __name__ == '__main__':
    format = '%(asctime)s:%(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    log = logging.getLogger('mylog')
    stream = logging.StreamHandler(stream=sys.stdout)
    log.addHandler(stream)

    test_pattern = {
        1: {'items': [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
            'ruleKey': 'color',
            'ruleValue': 'silver'},
        2: {'items': [['phone', 'blue', 'pixel'], ['computer', 'silver', 'phone'], ['phone', 'gold', 'iphons']],
            'ruleKey': 'type',
            'ruleValue': 'phone'}
        }
    mysolution = Solution()
    for _, test in test_pattern.items():
        myans = mysolution.countMatches(**test)
        log.info(f'Myans: {myans}')
    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
