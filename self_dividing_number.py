#Question: Easy
#A self-dividing number is a number that is divisible by every digit it contains.
#For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
#Also, a self-dividing number is not allowed to contain the digit zero.
#Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        div = []
        start = left
        end = right
        for i in range(start, end+1):
            value_str = str(i)
            add_value = True
            if i > 0:
                for value_chr in value_str:
                    value = int(value_chr)
                    if value == 0:
                        add_value = False
                    elif i % value != 0:
                        add_value = False
            if add_value == True:
                div.append(i)
        return div

left = 1
right = 22
result = Solution()
div_list = result.selfDividingNumbers(left=1, right=22)
print('self dividing number:', div_list)
