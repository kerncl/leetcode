// Question: Easy
/*
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
*/

#include <iostream>
#include <string>
class Solution{

public:
    std::string interpret(std::string command){
        std::string final ="";
        for(int i=0; i<command.size(); i++){
            if (command[i] == 'G'){
                NULL;
            }
        }
        return final;
    };
};


int main(){
    Solution mysolution;
    std::string command1 = "G()(al)";
    mysolution.interpret(command1);
    std::string ans1 = "Goal";
    std::string command2 = "G()()()()(al)";
    std::string ans2 = "Gooooal";
    std::string command3 = "(al)G(al)()()G";
    std::string ans3 = "alGalooG";
}