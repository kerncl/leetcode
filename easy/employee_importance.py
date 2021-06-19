#Question: Easy
"""
You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.
"""
import logging
from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_details = {e.id: (e.importance, e.subordinates) for e in employees}
        task = employee_details[id][0]
        sub = employee_details[id][1]
        temp_sub = list(sub)
        isFirst = True
        new_sub_sub = []
        while True:
            if isFirst:
                new_sub = sub
                isFirst = False
            elif not isFirst:
                new_sub = new_sub_sub
                new_sub_sub = []
            for subsub in new_sub:
                if employee_details[subsub][1]:
                    new_sub_sub.extend(employee_details[subsub][1])
            temp_sub.extend(new_sub_sub)
            if not bool(list(filter(None, new_sub_sub))):
                return sum(employee_details[_][0] for _ in temp_sub) + task




# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id!r},{self.importance!r},{self.subordinates!r}'


if __name__ == '__main__':
    format ='%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    employees1 = Employee(1, 5, [2, 3])
    employee2 = Employee(2, 3, [])
    employee3 = Employee(3, 3, [])
    id = 1
    employee4 = Employee(1, 5, [2, 3])
    employee5 = Employee(2, 3, [4])
    employee6 = Employee(3, 4, [])
    employee7 = Employee(4, 1, [])
    id2 = 1
    logging.info(f'Total importance value {result.getImportance([employee4, employee5, employee6, employee7], id)}')