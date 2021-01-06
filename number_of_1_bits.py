#Question: Easy
'''Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above, the input represents the signed integer. -3.
Follow up: If this function is called many times, how would you optimize it?
'''
import logging


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


if __name__ == '__main__':
    format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    n = 11111111111111111111111111111101
    n2 = 111
    n3 = 1011
    result = Solution()
    logging.info(f' Number of 1 : {result.hammingWeight(n3)}')