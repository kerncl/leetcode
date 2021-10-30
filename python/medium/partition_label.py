"""
You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

Return the array answer as described above.
"""
import logging
import sys
from typing import List
from collections import UserDict, OrderedDict


class Mydict(UserDict):

    def __init__(self):
        super().__init__()
        self.data = OrderedDict()

    def __setitem__(self, key, value):
        if key in self:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, item):
        return set(self.data[item])

    def __contains__(self, item):
        return int(item) in self.data

    def update(self, *tupl, **kwargs):
        for dic in tupl:
            for key, value in dic.items():
                self[key] = value
        if kwargs:
            raise NotImplemented('Doesnt implement')
            # for key, value in kwargs.items():
            #     self[key] = value


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mydict = Mydict()
        result = [0] * k
        [mydict.update({user:access}) for user, access in logs]
        # for user, access in logs:
        #     # mydict.update(user=access)
        #     mydict.update({user:access})
        #     # mydict.update([1,2,3])
        #     # mydict[user] = access
        for value in mydict.values():
            index = len(value) - 1
            result[index] += 1

        return result


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [([[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5, [0, 2, 0, 0, 0]),
                    ([[1, 1], [2, 2], [2, 3]], 4, [1, 1, 0, 0])]
    for logs, k, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.findingUsersActiveMinutes(logs, k)
        assert myresult == expected_result, log.error(f'Expected result: {expected_result}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
