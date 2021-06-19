#Questions: Easy
"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
"""
import logging
from string import punctuation, digits

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        reverse = ''
        reverse_str = S
        set_str = set(S)
        punc = set(punctuation+digits)
        for p in set_str.intersection(punc):
            reverse_str = reverse_str.replace(p, '')
        count = -1
        for alpha in S:
            if alpha in punctuation or alpha in digits:
                reverse += alpha
            else:
                reverse += reverse_str[count]
                count -= 1
        return reverse


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    S = 'ab-cd'
    S2 = 'a-bC-dEf-ghIj'
    S3 = 'Test1ng-Leet=code-Q!'
    result = Solution()
    logging.info(f'Proper: {S3} Reverse: {result.reverseOnlyLetters(S3)}')