#Question: Easy
"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?
"""
import logging


class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for value in range(1, N+1):
            value_str = str(value)
            if '3' in value_str or '4' in value_str or '7' in value_str:
                continue
            if '2' in value_str or '5' in value_str or '6' in value_str or '9' in value_str:
                count += 1
        return count


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    N = 10
    logging.info(f'There are {result.rotatedDigits(N)} good number in the range of {N}')