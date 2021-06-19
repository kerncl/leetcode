#Question: Easy
'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
'''
from typing import List
from collections import Counter
import logging


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # words = [word.rstrip("!?',;.").lower() for word in paragraph.split()]
        words = []
        for word1 in paragraph.split():
            if ',' in word1.rstrip("!?',;."):
                for word2 in word1.rstrip(','):
                    words.append(word2.rstrip("!?',;.").lower())
            else:
                words.append(word1.rstrip("!?',;.").lower())
        c_words = Counter(words)
        common = c_words.most_common(len(banned)+1)
        for item in common:
            if item[0] not in banned:
                return item[0]
        return ''


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    paragraph2 = "a, a, a, a, b,b,b,c, c"
    banned2 = ["a"]
    logging.info(f'The appear most word: {result.mostCommonWord(paragraph, banned)}')