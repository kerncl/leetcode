#Question: Easy
'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''
import logging


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if S == T:
            return True
        stack_s = []
        stack_t = []
        S = list(S[::-1])
        T = list(T[::-1])
        while S:
            temp_s = S.pop()
            if temp_s == '#':
                if len(stack_s):
                    stack_s.pop()
                continue
            stack_s.append(temp_s)
        while T:
            temp_t = T.pop()
            if temp_t == '#':
                if len(stack_t):
                    stack_t.pop()
                continue
            stack_t.append(temp_t)
        return ''.join(stack_s) == ''.join(stack_t)


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    result = Solution()
    S = "ab##"
    T = "c#d#"
    S2 = 'ab#c'
    T2 = 'ad#c'
    S3 = "y#fo##f"
    T3 = "y#f#o##f"
    logging.info(f' Are S and T same: {result.backspaceCompare(S3, T3)}')