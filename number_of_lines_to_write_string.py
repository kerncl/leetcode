# Question: Easy
'''
We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.
Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.
'''
from typing import List
import string


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        alpha = {abc: widths for abc, widths in zip(string.ascii_lowercase, widths)}
        length = 0
        final_list = [1,0]
        for char in S:
            length += alpha[char]
            if length > 100:
                final_list[0] += 1
                length = 0
                length += alpha[char]
        final_list[1]= length
        return final_list


widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
S = "abcdefghijklmnopqrstuvwxyz"
widths2 = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S2 = "bbbcccdddaaa"
widths3 =[5,7,4,7,6,7,9,5,8,8,5,10,9,10,2,5,7,9,3,8,8,8,10,2,2,9]
S3 = "lgrnv"
widths4 = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
S4 = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
result = Solution()
print(f'[Number of lines, unit] : {result.numberOfLines(widths3, S3)}')
