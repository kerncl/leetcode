"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""
import logging

def solution(a):
    if len(a) % 2:
        print('Odd len')
        return 0

    key_matching = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    left_s = a[:len(a)//2]
    right_s = a[len(a)//2:]

    left_s1 = []
    for i in range(1,len(left_s)):
        if key_matching.get(left_s[i-1]) != left_s[i]:
            left_s1.append(left_s[i-1])

    right_s1 = []
    for i in range(1,len(right_s)):
        if key_matching.get(right_s[i-1]) != right_s[i]:
            right_s1.append(right_s[i-i])


    return 1

def solution2(a):
    # find matching 1st
    brackets = ('()', '[]', '{}')
    remaining = []
    i = 1
    while i < len(a):
        if (a[i-1] + a[i]) not in brackets:
            remaining.append(a[i-1])
        else:
            i+=1
        if i >= len(a):
            break
        i += 1
    else:
        remaining.append(a[i-1])


    len_rem= len(remaining)
    print(remaining)
    for l,r in zip(range(len_rem//2, -1, -1), range(len_rem//2+1,len_rem+1)):
        print(f"{l}: {remaining[l-1]}, {r}:{remaining[r-1]}")
        if (remaining[l-1]+remaining[r-1]) not in brackets:
            return 0

    return 1

def solution3(a):
    # Stack

    brackets = ('()', '[]', '{}')
    stack = [a[0]]
    for i in range(1,len(a)):
        if (stack[-1] + a[i]) not in brackets:
            stack.append(a[i])
        else:
            stack.pop()
    if len(stack):
        return 0
    return 1




if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    s1 = "{[()()]}"
    s2 = "([)()]"
    s3 = "()[]{}"
    logging.info(f'{s1}: {solution3(s1)}')
    logging.info(f'{s2}: {solution2(s2)}')
    logging.info(f'{s3}: {solution2(s3)}')
