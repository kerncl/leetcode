# Question: Easy
"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
"""

import logging
import sys


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    log = logging.getLogger('mylog')
    stream = logging.StreamHandler(stream=sys.stdout)
    log.addHandler(stream)

    test_pattern = [("G()(al)", "Goal"),
                    ("G()()()()(al)", "Gooooal"),
                    ("(al)G(al)()()G", "alGalooG")]

    mysolution = Solution()
    for test, result in test_pattern:
        myresult = mysolution.interpret(test)
        assert myresult == result, log.error(f'Expected {result},but Received {myresult}')

    log.info('Done')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)

