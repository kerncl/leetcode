#Questions: easy
#Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.
#The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.
import string

class Solution:
    def generateTheString(self, n: int) -> str:
        alphabet = list(string.ascii_lowercase)
        word = ''
        if n % 2:
            for i in range(n):
                word += alphabet[0]
        else:
            word += alphabet[0]
            for i in range(n-1):
                word += alphabet[1]
        return word

n = 4
result = Solution()
output = result.generateTheString(n)
print('word:', output)




