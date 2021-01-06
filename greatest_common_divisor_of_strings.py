#Question: Easy
'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''
import logging


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(len(str2)):
            if i:
                pattern = str2[:-i]
            else:
                pattern=str2[:]
            pattern = str2[:(i+1)]
            pattern_len = len(pattern)
            search_index = 0
            while True:
                front = search_index*pattern_len
                back = search_index*pattern_len + pattern_len
                search_index += 1
                if back > len(str1):
                    break
                if str1[front:back] != pattern:
                    break
                else:
                    if back == len(str1):
                        return pattern
        return ''


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    str1 = 'ABCABC'
    str2 = 'ABC'
    str3 = 'ABABABAB'
    str4 = 'ABAB'
    str5 = 'LEET'
    str6 = 'CODE'
    str7 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str8 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    logging.info(f' Divider : {result.gcdOfStrings(str3, str4)}')