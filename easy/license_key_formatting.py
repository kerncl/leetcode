#Question: Easy
'''
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.
'''
import logging


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = ''.join(S.split('-'))
        remainder = len(s) % K
        list_s = []
        length = len(s)
        if remainder:
            list_s.append(s[:remainder].upper())
            length -= remainder
        while length > 0:
            remainder += K
            list_s.append(s[remainder - K : remainder].upper())
            length -= K
        return '-'.join(list_s)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%d/%m/%y-%H:%M:%S')
    result = Solution()
    S = "5F3Z-2e-9-w"
    K = 4
    S2 = "2-5g-3-J"
    K2 = 2
    logging.info(f'{result.licenseKeyFormatting(S, K)}')