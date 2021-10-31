// Question: Easy

/* Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive). */

#include <vector>
#include <iostream>
#include <tuple>
#include <array>

class Solution{
private:
    std::vector<int> _v {};

public:
    std::vector<int>buildArray(const std::vector<int>& nums){
        _v.clear();
        for(int i=0; i<nums.size(); i++){
            _v.push_back(nums[nums[i]]);
        }
        return _v;
    }
    void print_vec(){
        std::cout<< "{ ";
        for(const auto& value: _v){
            std::cout<<value<<", ";
        }
        std::cout<<" }"<<std::endl;
    }
};



int main(){
    Solution mysolution;
    const std::vector<int> nums1 {0, 2, 1, 5, 3, 4};
    const std::vector<int> ans1 {0, 1, 2, 4, 5, 3};
    mysolution.buildArray(nums1);
    mysolution.print_vec();
    const std::vector<int> nums2 {5, 0, 1, 2, 3, 4};
    const std::vector<int> ans2 {4, 5, 0, 1, 2, 3};
    mysolution.buildArray(nums2);
    mysolution.print_vec();
}