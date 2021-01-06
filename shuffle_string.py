#Question: easy
#Given a string s and an integer array indices of the same length.
#The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#Return the shuffled string.
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffledstr = {}
        count = 0
        for i in indices:
            shuffledstr[i]=s[count]
            count += 1
        #string = sorted(shuffledstr.items(), key=lambda x:x[0])
        print(shuffledstr)
        seperator = ""
        string = seperator.join([value for key,value in sorted(shuffledstr.items(), key=lambda x:x[0])])
        return str(string)

class Solution2:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle = [""]*len(s)   # shuffle --> list
        for i in range(len(indices)):
            shuffle[indices[i]] = s[i]
        return "".join(shuffle)


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
result = Solution()
shuffle = result.restoreString(s,indices)
print('New String:', shuffle)
result2 = Solution2()
shuffle2 = result2.restoreString(s,indices)
print('New String:', shuffle2)