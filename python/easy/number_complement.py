#Question: Easy
'''
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.
'''
import math

class Solution:
    def findComplement(self, num: int) -> int:
        power_bit = len(bin(num).lstrip('0b'))
        print(power_bit)
        mask = int(math.pow(2, power_bit))-1
        print(mask)
        return num^mask


num = 2
result = Solution()
print(f'Complement: {result.findComplement(num)}')
