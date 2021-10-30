#Question: Easy
"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
"""
import logging
import math

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count = 0
        for value in range(L, R+1):
            bit_count = bin(value).count('1')
            if bit_count in [2, 3, 5, 7, 11, 13, 17,19 ]:
                count +=1
        return count


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    L = 6
    R = 10
    L2=289051
    R2=294301
    result = Solution()
    logging.info(f'{result.countPrimeSetBits(L2, R2)} prime number of binary bit in the secquence ')
