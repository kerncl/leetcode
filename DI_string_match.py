#Question: easy
#Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#If S[i] == "I", then A[i] < A[i+1]
#If S[i] == "D", then A[i] > A[i+1]
from typing import List
import time


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        N = []
        i = 0
        j = 0
        for value in S:
            if value == 'I':
                N.append(i)
                i += 1
            elif value == 'D':
                N.append(n-j)
                j += 1
        N.append(i)
        return N


s = "IDID"
result = Solution()
start = time.perf_counter_ns()
dis = result.diStringMatch(s)
time1 = time.perf_counter_ns() - start
print('Dis:', dis)
print('Total use time {sec} ns' .format(sec=time1))