#Question:
'''
Given an array of unique integers salary where salary[i] is the salary of the employee i.
Return the average salary of employees excluding the minimum and maximum salary.
'''
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[_] for _ in range(1,len(salary)-1)) / (len(salary)-2)

class Solution2:
    def average(self, salary: List[int]) -> float:
        avg = (sum(salary) - min(salary) -max(salary)) /(len(salary)-2)
        return avg

salary = [6000,5000,4000,3000,2000,1000]
result = Solution()
print(f'Average Salary: {result.average(salary)}')
result2 = Solution2()
print(f'Average Salary: {result2.average(salary)}')
