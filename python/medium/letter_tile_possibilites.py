"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
"""
import logging
import sys
from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []
        for _ in range(len(tiles)):
            result.extend([_ for _ in permutations(tiles, _+1)])
        return len(set(result))


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s] %(message)s'

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setLevel(logging.INFO)
    stream.setFormatter(logging.Formatter(format))
    log.addHandler(stream)

    test_pattern = [("AAB", 8),
                    ("AAABBC", 188),
                    ("V", 1)]

    for tiles, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.numTilePossibilities(tiles)
        assert myresult == expected_result, log.error(f'Expected result: {expected_result}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)