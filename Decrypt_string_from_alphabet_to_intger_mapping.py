#Question: easy
#Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
#Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#Return the string formed after mapping.
#It's guaranteed that a unique mapping will always exist.\
# 97 - a
# 122 - z
class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        rletter = ''
        ishash = False
        while i>=0:
            if ishash == False:
                if s[i] == '#':
                    ishash = True
                    i-= 1
                else:
                    unicode = int(int(s[i])+96)
                    rletter += chr(unicode)
                    i -= 1
            elif ishash == True:
                unicode = int(s[i-1]+s[i])+96
                rletter += chr(unicode)
                i -= 2
                ishash = False
        letter = ''.join(reversed(rletter))
        return letter


s = "1326#"
result = Solution()
string = result.freqAlphabets(s)
print('String :', string)