#Question: Easy
#Given an array of integers nums.
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#Return the number of good pairs.


from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                temp = nums[i]
                if temp == nums[j]:
                    count += 1
        return count

class Solution2:
    def numIdenticalPairs(self,nums: List[int])-> int:
        listVals = {}
        for i in nums:
            if i not in listVals:
                listVals[i]=0
            listVals[i]+=1
        numberPairs= 0

        for i in listVals:
            numberPairs += (listVals[i]*(listVals[i]-1))/2   #Sn formula
        return int(numberPairs)


number = [1, 2, 3, 1, 1, 3]
result = Solution()
print('Result1:', result.numIdenticalPairs(number))
result2=Solution2()
print('Result2:', result2.numIdenticalPairs(number))

