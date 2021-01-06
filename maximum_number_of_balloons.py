#Question: Easy
"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""
import logging


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        list_alpha = []
        list_alpha.append(text.count('b'))
        list_alpha.append(text.count('a'))
        list_alpha.append(text.count('l')//2)
        list_alpha.append(text.count('o')//2)
        list_alpha.append(text.count('n'))
        return min(list_alpha)


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    text = "nlaebolko"
    text2 = "loonbalxballpoon"
    text3 = 'leetcode'
    logging.info(f'{result.maxNumberOfBalloons(text3)} Number of repeater balloon in text')