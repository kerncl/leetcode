#Question: Easy
'''
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.
'''
import logging


class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = text.count(' ')
        words = [word for word in text.split(' ') if word]
        if len(words) == 1:
            return words[0] + ' '*space_count
        space = space_count // (len(words) -1 )
        remainder = space_count % (len(words) - 1)
        return f"{' '*space}".join(words) + ' '*remainder


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    text = "  this   is  a sentence "
    text2 = " practice   makes   perfect"
    logging.info(f'Reformat string: {result.reorderSpaces(text2)}')