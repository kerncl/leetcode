#Question Easy:
'''
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
'''
import logging
import string
from collections import deque


class Solution:
    def modifyString(self, s: str) -> str:
        list_s = s.split('?')
        alpha = string.ascii_lowercase
        final_string = list_s[0] if list_s[0] else alpha[0]
        for index in range (1,len(list_s)):
            if len(list_s[index]):
                for alp in alpha:
                    if final_string[-1] != alp and list_s[index][0] != alp:
                        final_string += alp + list_s[index]
                        break
            else:
                for alp in alpha:
                    if final_string[-1] != alp:
                        final_string += alp + list_s[index]
                        break
        return final_string if list_s[0] else final_string[1:]


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    s = "??yw?ipkj?"
    s2 = "?zs"
    s3 = 'a?'
    s4 = 'a?z'
    s5 = 'y?z'
    s6 = '?y??ty'
    result = Solution()
    logging.info(f'New string: {result.modifyString(s6)}')