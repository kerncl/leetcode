"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

"""
import logging
import sys
from typing import List
from collections import Counter, defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        found = 0
        list_s = list(s)
        counter_s = Counter(s)
        while words:
            word = words[-1]
            if word in s:
                words.pop()
                found += 1
                continue

            counter_word = Counter(word)
            loop = True
            for alpha, count in counter_word.items():
                count_s = counter_s.get(alpha, None)
                if count_s:
                    if count > count_s:
                        words.pop()
                        loop = False
                        break
                else:
                    words.pop()
                    loop = False
                    break

            if not loop:
                continue

            temp_index = 0
            temp_list = list_s.copy()
            for alpha in word:
                try:
                    index = temp_list.index(alpha)
                    temp_list.remove(alpha)
                    temp_list.insert(index, '-')
                    if temp_index > index:
                        words.pop()
                        break
                except:
                    words.pop()
                    break
            else:
                words.pop()
                found +=1

        return found


class Node:
    def __init__(self, word):
        self.word = word
        self.index = 0

class Solution2:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            startingChar = word[0]
            buckets[startingChar].append(Node(word))

        ans = 0
        for c in s:
            currBucket = buckets[c]
            buckets[c] = []
            for node in currBucket:
                node.index += 1  # Point to next character of node.word
                if node.index == len(node.word):
                    ans += 1
                else:
                    startingChar = node.word[node.index]
                    buckets[startingChar].append(node)
        return ans

if __name__ == '__main__':
    format = '%(asctime)s [%(levelname)s] :%(message)s'
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    test_pattern = [("abcde", ["a", "bb", "acd", "ace"], 3),
                    ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], 2)]
    for s, words, expected_result in test_pattern:
        solution = Solution()
        myresult = solution.numMatchingSubseq(s=s, words=words)
        assert myresult == expected_result, log.error(f'Expected result: {expected_result}, but received: {myresult}')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
