"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
"""
import logging
import sys


class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(_) for _ in n])


class Solution2:
    def minPartitions(self, n: str) -> int:
        return max([int(_) for _ in set(n)])


class Solution3:
    def minPartitions(self, n: str) -> int:
        return max(map(int, set(n)))


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    log.addHandler(stream)
    result = Solution()
    test_pattern = ['32', '82734', "27346209830709182346"]
    expected_result_list = [3, 8, 9]
    for pattern, expected_result in zip(test_pattern, expected_result_list):
        myresult = result.minPartitions(pattern)
        log.info(f'result: {myresult}')
        assert expected_result == myresult

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)