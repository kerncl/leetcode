#Question: Easy
'''
Write a function that takes a string as input and reverse only the vowels of a string.
'''
import logging


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        stack = [alpha for alpha in s if alpha.lower() in vowel]
        final = ''
        for alpha in s:
            if alpha.lower() in vowel:
                final += stack.pop()
                continue
            final += alpha
        return final


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    s = "leetcode"
    s2 = 'aA'
    logging.info(f'Reversed of s : {result.reverseVowels(s2)}')