// Question: Easy
/*
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
*/
#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>

class Solution{
public:
    int countkDifference(std::vector<int>& nums, int k){
        int couts=0;
        for(int i=0; i<nums.size(); i++){
            for(int j=1; j<nums.size(); j++){
                if (i>j) continue;
                if (std::abs(nums[i]-nums[j]) == k){
                    std::cout<<nums[i]<<"-"<<nums[j] << ": " <<couts<<std::endl;
                    couts+=1;
                }
            }
        }
        return couts;
    }
};


int main(){

    Solution mysolution;
    std::vector<int> nums1 = {1,2,2,1};
    int k1 = 1;
    int myans = mysolution.countkDifference(nums1, k1);
    std::cout<<"My ANS :" << myans << std::endl;
}