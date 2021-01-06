#Question: Easy
'''
Given a sentence that consists of some words separated by a single space, and a searchWord.
You have to check if searchWord is a prefix of any word in sentence.
Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).
If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.
A prefix of a string S is any leading contiguous substring of S.
'''
import re

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index_w, word in enumerate(sentence.split(' ')):
            if len(searchWord) > len(word):
                continue
            for index, alpha in enumerate(searchWord):
                if alpha != word[index]:
                    break
                if len(searchWord) -1 == index:
                    return index_w+1
        return -1


class Solution2:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        pattern = re.compile(r''+searchWord)
        for index, word in enumerate(sentence.split(' ')):
            if pattern.match(word):
                return index+1
        return -1

sentence = "i love eating burger"
searchWord = "burg"
sentence2 = "this problem is an easy problem"
searchWord2 = "pro"
sentence3 = "i am tired"
searchWord3 = "you"
result = Solution()
print(f'Found searchWord in Sentence with {result.isPrefixOfWord(sentence, searchWord)} index')
result2 = Solution2()
print(f'Found searchWord in Sentence with {result2.isPrefixOfWord(sentence2, searchWord2)} index')