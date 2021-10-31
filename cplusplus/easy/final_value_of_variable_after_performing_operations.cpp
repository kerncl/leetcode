// Question: Easy

/*
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
*/
#include <vector>
#include <string>
#include <iostream>


class Solution{
public:
    int finalValueAfterOperations(std::vector<std::string>& operations){
        int init_val = 0;
        for (const std::string& operation:operations){
            if (operation.find("+") != std::string::npos){
                init_val++;
                continue;
            }
            init_val--;
        }
        return init_val;
    }
};


int main(){
    Solution mysolution;
    std::vector<std::string> operations1 = {"--X", "X++", "X++"};
    int ans1 = 1;
    int myans1 = mysolution.finalValueAfterOperations(operations1);
    std::cout<< "ANS 1:" << myans1 << std::endl;
    std::vector<std::string> operations2 = {"++X", "++X", "X++"};
    int ans2 = 0;
    std::vector<std::string> operations3 = {"X++", "++X", "--X","X--"};
    int ans3 = 0;
}