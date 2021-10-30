#Question: hard
#A password is considered strong if below conditions are all met:
#It has at least 6 characters and at most 20 characters.
#It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
#It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
#Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.
#Insertion, deletion or replace of any one character are all considered as one change.
import time
import string

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        count = 0
        alphabet_L = list(string.ascii_lowercase)
        alphabet_U = list(string.ascii_uppercase)
        digit = list(string.digits)
        alphabet_L_bool = False
        alphabet_U_bool = False
        digit_bool = False
        overfloat = False
        tooshort = True
        # 1st Condition
        if len(s) < 6:
            count = abs(6 - len(s))
            tooshort = True
        elif len(s) > 20:
            count = abs(20 - len(s))
            overfloat = True

        #if count < 2:
            # 2nd Condition
        if set(s).intersection(set(alphabet_L)):
            alphabet_L_bool = True
        if set(s).intersection(set(alphabet_U)):
            alphabet_U_bool = True
        if set(s).intersection(set(digit)):
            digit_bool = True
        if not (alphabet_U_bool and alphabet_L_bool and digit_bool) and tooshort:
            pass
        elif not (alphabet_U_bool | alphabet_L_bool | digit_bool) and tooshort:
            count += 1

        # 3rd Condition
        repeat = 1
        temp = ''
        repeat_bool = False
        reset = False
        s = list(s)
        s.extend(['']*2)
        repeat_count = 0
        for char in s:
            if not repeat_bool:
                if repeat > 20:
                    repeat = 20
                replace = repeat // 3
                repeat_count += replace
                if reset:
                    repeat = 1
            if temp != char:
                temp = char
                reset = True
                repeat_bool = False
            else:
                repeat += 1
                repeat_bool = True
        if repeat_count != 0:
            count += repeat_count
        if overfloat:
            if alphabet_U_bool and alphabet_L_bool and digit_bool:  # 3 True
                if repeat_count > 0:
                    #count -= 1
                    pass
            elif (alphabet_L_bool ^ alphabet_U_bool ^ digit_bool):    #2 False
                count += 2
                if repeat_count > 2:
                    count -= 2
                elif repeat_count > 0:
                    count -= 1
            elif not (alphabet_L_bool & alphabet_U_bool & digit_bool):  #1 False
                count += 1
                if repeat_count > 0:
                    count -= 1
        return count



pw = input('Please enter your password\t')
result = Solution()
start = time.perf_counter_ns()
chng = result.strongPasswordChecker(pw)
end = time.perf_counter_ns() - start
print('Number of change need to be done:', chng)
print('Total use time {sec} ms' .format(sec=end/1000))