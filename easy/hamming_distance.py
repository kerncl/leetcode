#Question: easy
#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#Given two integers x and y, calculate the Hamming distance.
import time


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return abs(x.bit_length()-y.bit_length())

class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        bx=(format(x, '032b'))
        by=(format(y, '032b'))
        dist = sum([int(bx[i]!=by[i]) for i in range(len(bx))])
        return dist

x = 93
y = 73
result = Solution()
start = time.perf_counter_ns()
distance = result.hammingDistance(x,y)
time1 = time.perf_counter_ns() - start
print('Humming distance:', distance)
print('Total use time:', time1)
result2 = Solution2()
start = time.perf_counter_ns()
distance2 = result2.hammingDistance(x,y)
time2 = time.perf_counter_ns() - start
print('Humming distance:', distance2)
print('Total use time:', time2)
