#Question: Easy
'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''
import logging
import string

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        alpha_dict = {a:i+1 for i, a in enumerate(string.ascii_uppercase)}
        for index, alpha in enumerate(s[::-1]):
            ans += (26**index) * alpha_dict[alpha]
        return ans


if __name__ == '__main__':
    format= '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    s = 'ZY'
    logging.info(f'Current at coloumn {result.titleToNumber(s)}')