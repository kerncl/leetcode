#Question:
'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        s_split = s.split(" ")
        for text in s_split:
            list_text = list(text)
            for _ in range(len(text)):
                output += list_text.pop()
            output += " "
        return output.strip()


result = Solution()
input_str = "Let's take LeetCode contest"
print(result.reverseWords(input_str))