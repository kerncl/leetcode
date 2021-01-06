#Questions: Easy
'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
'''
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        list_word = []
        for word in words:
            row1_status = True
            row2_status = True
            row3_status = True
            for alpha in word:
                if alpha.lower() not in row1:
                    row1_status = False
                if alpha.lower() not in row2:
                    row2_status = False
                if alpha.lower() not in row3:
                    row3_status = False
            if row1_status or row2_status or row3_status:
                list_word.append(word)
        return list_word


words = ["Hello", "Alaska", "Dad", "Peace"]
result = Solution()
print(f'words: {result.findWords(words)}')
