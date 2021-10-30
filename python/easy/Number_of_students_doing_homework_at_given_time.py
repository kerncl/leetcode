#Question: easy
#Given two integer arrays startTime and endTime and given an integer queryTime.
#The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
#Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        busy = 0
        for start, end in zip(startTime,endTime):
            if start <= queryTime <= end:
                busy += 1
        return busy


startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5
result = Solution()
busy = result.busyStudent(startTime,endTime,queryTime)
print('No.of busy student:', busy)