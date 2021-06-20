"""
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
"""
import logging
import sys
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        boxes = list(map(int, boxes))
        for current_index in range(len(boxes)):
            total = 0
            for i, _ in enumerate(boxes):
                if current_index == i:
                    # skip if same index
                    continue
                if _:
                    total += abs(current_index - i)
            result.append(total)
        return result


class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        boxes = list(map(int, boxes))
        for current_index in range(len(boxes)):
            result.append(sum(map(lambda box, x,y: abs(x -y) if box else 0,
                                  boxes,
                                  range(len(boxes)),[current_index]*len(boxes))))
        return result


class Solution3:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        eval_string = '0'
        loc = {}
        if len(boxes) <= 1:
            return [0]
        # formula
        boxes = list(map(int, boxes))
        for index, _ in enumerate(boxes):
            if _:
                eval_string += f'+abs({index} - %(current_index)i)'
        formula = 'current_result =' + eval_string.strip()
        # iter
        for current_iter in range(len(boxes)):
            exec(formula%{'current_index':current_iter}, globals(), loc)
            result.append(loc['current_result'])
        return result


if __name__ == '__main__':
    format = '%(asctime)s [%(levelname)s]: %(message)s'
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [('110', [1, 1, 3]), # boxes, expected result
                    ('001011', [11, 8, 5, 4, 3, 4]),
                    ('0', [0]),
                    ('00', [0, 0])]
    for boxes, expected_result in test_pattern:
        result = Solution3()
        myresult = result.minOperations(boxes=boxes)
        assert myresult == expected_result,\
            log.error(f'Expected result {expected_result}, but obtain {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
