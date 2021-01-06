#Question: Easy
'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
'''
import logging


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for width in range(1, len(s)//2+1):
            if not len(s) % width:
                if s[:width]*(len(s)//width) == s:
                    return True
        return False


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    s = "abab"
    s2 = "abcabcabcabc"
    s3 = "abac"
    result = Solution()
    logging.info(f'Is repeated sub string pattern: {result.repeatedSubstringPattern(s)}')