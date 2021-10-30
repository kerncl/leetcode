"""
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
"""
import logging
import sys
import math
from typing import List
from collections import deque


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        length_result = int(math.log(label + 1) / math.log(2) + 0.5)
        result = deque()
        # i_inrow = 0
        for n_row in range(length_result, 0, -1):
            max_numinrow = int(math.pow(2, n_row) - 1)
            min_numinrow = int(math.pow(2, n_row - 1))
            if n_row % 2:
                # odd : start from left
                i_inrow = label - min_numinrow + 1
                result.appendleft(label)
                label = int(math.pow(2, n_row - 1) - 1) - int(i_inrow // 2)
                pass
            else:
                # even: start from right
                i_inrow = max_numinrow - label
                result.appendleft(label)
                label = int(math.pow(2, n_row - 2)) + int(i_inrow // 2)
                pass
        return list(result)


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s] %(message)s'

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [(14, [1, 3, 4, 14]),
                    (26, [1, 2, 6, 10, 26]),
                    (16, [1, 3, 4, 15, 16])]
    for label, expected in test_pattern:
        solution = Solution()
        myresult = solution.pathInZigZagTree(label)
        assert myresult == expected, log.error(f'Expected result: {expected}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
