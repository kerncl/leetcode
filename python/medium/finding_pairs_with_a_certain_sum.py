"""
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
"""
from typing import List
from collections import defaultdict
import logging


# format = '%(asctime)s - %(message)s'
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%D %H:%M:%S')
log = logging.getLogger('mylog')
stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
log.addHandler(stream)


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.loop1 = nums1
        self.loop2 = nums2
        self.modify = self.loop2
        if len(nums2) > len(nums1):
            self.loop1 = nums2
            self.loop2 = nums1
            self.modify = self.loop1

    def add(self, index: int, val: int) -> None:
        self.modify[index] += val

    def count(self, tot: int) -> int:
        count = 0
        for num1 in self.loop1:
            if num1 > tot: continue
            for num2 in self.loop2:
                if num1 + num2 == tot:
                    count+=1
        return count
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)


class FindSumPairs2:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.dictnums2 = defaultdict(int)

        for num in nums2:
            self.dictnums2[num] += 1

    def add(self, index: int, val: int) -> None:
        self.dictnums2[self.nums2[index]] -= 1
        self.dictnums2[self.nums2[index] + val] +=1

    def count(self, tot: int) -> int:
        return sum((self.dictnums2[tot - num] for num in self.nums1))



if __name__ == '__main__':
    obj = FindSumPairs2(nums1=[1, 1, 2, 2, 2, 3], nums2=[1, 4, 5, 2, 5, 4])
    assert obj.count(7) == 8, log.error(f'Expected value: 8, but received {7}')
    obj.add(index=3, val=2)
    assert obj.count(8) == 2, log.error(f'Expected value: 8, but received {2}')
    assert obj.count(4) == 1, log.error(f'Expected value: 8, but received {1}')
    obj.add(index=0, val=1)
    obj.add(index=1, val=1)
    assert obj.count(7) == 11, log.error(f'Expected value: 8, but received {11}')