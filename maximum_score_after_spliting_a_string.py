#Question: Easy
"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""
import logging


class Solution:
    def maxScore(self, s: str) -> int:
        for index in range(1,len(s)):
            current = s[0:index].count('0') + s[index:].count('1')
            if index == 1:
                temp_max = current
            temp_max = max(current, temp_max)

        return temp_max

class Solution2:
    def maxScore(self, s:str) -> int:
        score = 0
        zeros = 0
        ones = s.count('1')

        for i in range(len(s)-1):
            if s[i] == '0':
                zeros +=1
            else:
                ones -=1
            score = max(score, ones+zeros)
        return score

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
    s = "011101"
    s2 = '00111'
    result = Solution()
    logging.info(f'max score: {result.maxScore(s)}')