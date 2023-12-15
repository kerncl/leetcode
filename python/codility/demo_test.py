import logging


class Solution:
    pass

def solution(A):
    A.sort()
    max = A[-1]
    if max < 0:
        return 1
    for i in range(1, max+1):
        try:
            A.index(i)
        except ValueError as e:
            return i
    return i + 1


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    A = [1, 3, 6, 4, 1, 2]
    B = [1, 2, 3]
    C = [-1, -3]
    D = [1, 2, 3, 4, 6, 7, 8]
    E = [-1, -4, 6, 8, 1, 2, 5]
    logging.info(f'Smallest number >0 doesnt occurs in A: {solution(A)}')
    logging.info(f'Smallest number >0 doesnt occurs in B: {solution(B)}')
    logging.info(f'Smallest number >0 doesnt occurs in C: {solution(C)}')
    logging.info(f'Smallest number >0 doesnt occurs in D: {solution(D)}')
    logging.info(f'Smallest number >0 doesnt occurs in E: {solution(E)}')

