"""
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
"""
import logging
import sys
from typing import List
from collections import Counter


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # count = sorted(Counter(groupSizes).items(), key=itemgetter(0))
        count = Counter(groupSizes)
        list_index = sorted(count.keys())
        result = [[] for _ in list_index]

        for i, size in enumerate(groupSizes):
            result[list_index.index(size)].append(i)

        for i in list_index:
            index = list_index.index(i)
            if len(result[index]) != i:
                modify_list = result.pop(index)
                for _ in range(len(modify_list) // i):
                    result.append(modify_list[_ * i:(_ + 1) * i])

        return result


class Solution2:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # count = sorted(Counter(groupSizes).items(), key=itemgetter(0))
        result = []
        count = Counter(groupSizes)
        for key in count.keys():
            count[key] = []
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        for key, value in count.items():
            for _ in range(len(value)//key):
                result.append(value[_*key:(_+1)*key])
        return result


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    format = '%(asctime)s [%(levelname)s] : %(message)s'
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([3, 3, 3, 3, 3, 1, 3], [[0, 1, 2], [3, 4, 6], [5]]),
                    ([2, 1, 3, 3, 3, 2], [[0, 5], [1], [2, 3, 4]]),
                    ([3, 4, 3, 3, 4, 4, 3, 4, 3, 3], [[0, 2, 3], [6, 8, 9], [1, 4, 5, 7]])
                    ]

    for groupsize, expected_result in test_pattern:
        solution = Solution2()
        myresult = solution.groupThePeople(groupsize)
        assert myresult == expected_result, \
            log.error(f'Expected result {expected_result}, but received {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
