#Question: Easy
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
'''
import logging


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        orig = n

        for i in range(1,1000):
            if guess(n) == 0:
                return n

            elif guess(n) == -1:
                n -= int(orig/2 **i) if int(orig/2 ** i) else 1
            elif guess(n) == 1:
                n+= int(orig/ 2** i) if int(orig/2 ** i) else 1
        return 0


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    n = 2
    pick = 2
    logging.info(f'What you guess: {result.guessNumber(n)}')