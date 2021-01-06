#Question: Easy
'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
'''
class Solution:
    def removeDuplicates(self, S: str) -> str:
        repeated = True
        S = list(S)
        while repeated:
            temp = ''
            for index, alpha in enumerate(S):
                if temp == alpha:
                    S.pop(index-1)
                    S.pop(index-1)
                    if not len(S):
                        repeated = False
                    break
                elif index == len(S)-1:
                    repeated = False
                temp = alpha
        return ''.join(map(str,S))

class StackSolution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        ans = ""
        for i in S:
            if stack:
                if stack[-1] == i:
                    stack.pop(-1)
                else:
                    stack.append(i)
            else:
                stack.append(i)

        for i in stack:
            ans += i
        return ans
s = 'aaaaaaaa'
result = Solution()
print(f'final result {result.removeDuplicates(s)}')
result2 = StackSolution()
print(f'final result {result2.removeDuplicates(s)}')