#Question: Easy
"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
"""
import logging
import sys
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '+' in operation else -1 for operation in operations)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    log = logging.getLogger('mylog')
    stream = logging.StreamHandler(sys.stdout)
    log.addHandler(stream)

    test_pattern = [(['--X', 'X++', 'X++'], 1),
                    (['++X', '++X', 'X++'], 3),
                    (['X++', '++X', '--X', 'X--'], 0)]
    mysolution = Solution()
    for test, result in test_pattern:
        myresult = mysolution.finalValueAfterOperations(test)
        assert myresult == result, log.error(f'Expected: {result}, but {myresult}')

    log.info('DONE')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)