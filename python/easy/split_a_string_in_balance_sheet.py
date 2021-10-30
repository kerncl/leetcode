#Question: easy
#Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#Given a balanced string s split it in the maximum amount of balanced strings.
#Return the maximum amount of splitted balanced strings.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        pattern = 0
        count = 0
        for letter in s:
            if letter == 'L':
                pattern -= 1
            else:
                pattern +=1
            if pattern == 0:
                count += 1
        return count


s = "RLRRRLLRLL"
result = Solution()
samepattern = result.balancedStringSplit(s)
print('Number of balance sheet:', samepattern)