//Question Easy
/* 
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
*/
#include <vector>
#include <iostream>

void print_vec(const std::vector<int>& vec){
    std::cout<<"{ ";
    for (const auto& i:vec){
        std::cout<<i<<", ";
    }
    std::cout<<"}"<<std::endl;
}

class Solution{
public:
    std::vector<int> getConcatenation(std::vector<int>& nums){
        nums.insert(nums.end(), nums.begin(), nums.end());
        return nums;
    }
};

class Solution2{
public:
    std::vector<int>getConcatenation(std::vector<int>& nums){
        std::vector<int> result(2*nums.size());
        for(int i=0; i<nums.size(); i++){
            result[i] = nums[i];
            result[i+nums.size()] = nums[i];
        }
        return result;
    }
};


int main(){
    Solution mysolution;
    std::vector<int> nums1 = {1,2,1};
    std::vector<int> ans1 = {1,2,1,1,2,1};
    auto ans11 = mysolution.getConcatenation(nums1);
    print_vec(ans11);
    std::vector<int> nums2 = {1,3,2,1};
    std::vector<int> ans2 {1,3,2,1,1,3,2,1};
    Solution2 mysolution2;
    auto ans22 = mysolution2.getConcatenation(nums2);
    print_vec(ans22);
}