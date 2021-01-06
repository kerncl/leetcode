#Question: Easy
"""
Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
"""
import logging
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words = sorted(words, key=len)
        for i in range (len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.INFO)
    words = ["mass", "as", "hero", "superhero"]
    result = Solution()
    logging.info(f'Output string {result.stringMatching(words)}')