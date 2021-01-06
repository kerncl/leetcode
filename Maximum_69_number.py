#Question: easy
#Given a positive integer num consisting only of digits 6 and 9.
#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
class Solution:
    def maximum69Number(self, num: int) -> int:
        max_number = num
        list_num = list(str(num))
        count = 0
        for digit in list_num:
            if digit == '6':
                list_num[count] = '9'
                max_number = int("".join(list_num))
                break
            count += 1

        return max_number


num = 9669
result = Solution()
max_number = result.maximum69Number(num)
print('THe maximum number:', max_number)