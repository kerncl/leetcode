//Question: Easy
/*
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
*/

#include <iostream>
#include <vector>
#include <string>
#include <map>

class Solution{

public:
    int countMatches(std::vector<std::vector<std::string>>& items, std::string ruleKey, std::string ruleValue){
        int index;
        int cout {0};
        if (ruleKey.compare("type") == 0){
            index = 0;
        }else if (ruleKey.compare("color") == 0){
            index = 1;
        }else if (ruleKey.compare("name") == 0){
            index = 2;
        }
        for (auto& item:items){
            if (ruleValue.compare(item[index]) == 0){
                cout+=1;
            }
        }
        return cout;
    }
};

class Solution2{
private:
    std::map<std::string,int> mp {{"type",0}, {"color",1}, {"name",2}};
public:
    int countMatches(std::vector<std::vector<std::string>>& items, std::string ruleKey, std::string ruleValue){
        int index = mp[ruleKey];
        int cout = 0;
        for(auto& item:items){
            if(ruleValue.compare(item[index])==0){
                cout+=1;
            }
        }
        return cout;
    }
};

int main(){
    Solution2 mysolution;
    std::vector<std::vector<std::string>> items {{"phone","blue","pixel"}, {"computer", "silver", "phone"}, {"phone","gold","iphone"}};
    std::string ruleKey = "type";
    std::string ruleValue = "phone";
    int ans = mysolution.countMatches(items, ruleKey, ruleValue);
    std::cout<<"My ans :" << ans << std::endl;
}