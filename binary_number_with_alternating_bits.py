#Question: Easy
'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
'''
import logging


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n_bit = list(bin(n))[2:]
        for index in range(len(n_bit)-1):
            if n_bit[index] == n_bit[index+1]:
                return False
        return True


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    n = 11
    n2 = 5
    logging.info(f'has Alternating Bits : {result.hasAlternatingBits(n)}')