#Question: easy
#A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
#Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
#Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        S = list(S)
        status = 0
        start_index = 1
        bracket = []
        for i in range(len(S)):
            if S[i] == "(":
                status += 1
            elif S[i] == ")":
                status -= 1
            if status == 0:
                current_index = i
                bracket.extend(S[start_index:current_index])
                start_index = i + 2
                status = 0
        inner_bracket = "".join(bracket)
        return inner_bracket

s = "(()())(())(()(()))"
result = Solution()
bracket = result.removeOuterParentheses(s)
print('Number of bracket:', bracket)