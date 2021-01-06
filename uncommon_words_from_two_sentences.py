#Question: Easy
"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.
"""
import logging
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        total_list = A.split(' ') + B.split(' ')
        uncommon_list = []
        for value in set(total_list):
            if total_list.count(value) == 1:
                uncommon_list.append(value)
        return uncommon_list


if __name__ == '__main__':
    format = "%(asctime)s %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    A = "this apple is sweet"
    B = "this apple is sour"
    A2 = "apple apple"
    B2 = "banana"
    result = Solution()
    logging.info(f'Uncommon list: {result.uncommonFromSentences(A2, B2)}')
