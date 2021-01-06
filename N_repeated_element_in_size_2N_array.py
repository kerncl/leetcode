#Question: easy
#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#Return the element repeated N times.
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = len(A)/2
        set_list = set(A)
        for value in set_list:
            if count == A.count(value):
                break
        return value

class Solution2:
    def repeatedNTimes(self, A: List[int]) -> int:
        found = set()
        for it in A:
            if it in found:
                return it
            found.add(it)


input_list = [5, 1, 5, 2, 5, 3, 5, 4]
result = Solution()
no_repeater = result.repeatedNTimes(input_list)
print('1. The no. repearter in the list are:', no_repeater)
result2 = Solution2()
no_repeater2 = result2.repeatedNTimes(input_list)
print('2. The no. repearter in the list are:', no_repeater2)