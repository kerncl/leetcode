#Question: Easy
'''
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
'''
import logging
from collections import deque


class Solution:
    def makeGood(self, s: str) -> str:
        s_list = deque(s)
        ans = deque([])
        while s_list:
            temp = s_list.popleft()
            if str(temp).isupper() or (ans and str(ans[len(ans)-1]).isupper()):
                if ans and ans[len(ans)-1].lower() == str(temp).lower():
                    if ans[len(ans)-1] == str(temp):
                        ans.append(temp)
                        continue
                    ans.pop()
                    continue
                elif s_list and str(temp).lower() == s_list[0]:
                    if str(temp) == s_list[0]:
                        ans.append(temp)
                        continue
                    s_list.popleft()
                    continue
            ans.append(temp)

        return ''.join(ans)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    s = 'leEeetcode'
    s2 = 'abBAcC'
    s3 = 'Pp'
    s4 = 'mC'
    s5 = 'RLlr'
    s6 = '"kkdsFuqUfSDKK"'
    s7 = 'MHTLuuHhUUlthmQwUWq'
    result = Solution()
    logging.info(f'final string: {result.makeGood(s)}')