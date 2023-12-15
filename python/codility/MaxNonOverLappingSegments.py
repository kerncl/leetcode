"""
Located on a line are N segments, numbered from 0 to N − 1, whose positions are given in arrays A and B. For each I (0 ≤ I < N) the position of segment I is from A[I] to B[I] (inclusive). The segments are sorted by their ends, which means that B[K] ≤ B[K + 1] for K such that 0 ≤ K < N − 1.

Two segments I and J, such that I ≠ J, are overlapping if they share at least one common point. In other words, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to find the size of a non-overlapping set containing the maximal number of segments.

For example, consider arrays A, B such that:

    A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10
The segments are shown in the figure below.



The size of a non-overlapping set containing a maximal number of segments is 3. For example, possible sets are {0, 2, 3}, {0, 2, 4}, {1, 2, 3} or {1, 2, 4}. There is no non-overlapping set with four segments.

Write a function:

def solution(A, B)

that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

For example, given arrays A, B shown above, the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..30,000];
each element of arrays A and B is an integer within the range [0..1,000,000,000];
A[I] ≤ B[I], for each I (0 ≤ I < N);
B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).
"""
def get_next_available_start(index, a, b):
    s = []
    for _ in range(index + 1, len(a)):
        if a[_] > b[index]:
            s.append(_)
    return s

def get_possible_non_overlapping(index, a, b):
    path = []
    next_v = get_next_available_start(index, a, b)
    for next_index in next_v:
        inner_path = [next_index]
        inner_path += get_possible_non_overlapping(next_index, a, b)
        path.extend(inner_path)
    return path

def solution2(a,b):
    overall = []
    for i in range(len(a)):
        overall.append([i] + get_possible_non_overlapping(i, a, b))

    return overall


def solution(a, b):
    overall = []
    for i in range(len(a)):
        non_overlap = [i]
        while i < len(a):
            if a[i] > b[i-1]:
                non_overlap.append(i)
            i += 1


        if len(non_overlap) > 1:
            overall.append(non_overlap)
    return overall

if __name__ == '__main__':
    a = [1, 3, 7, 9, 9]
    b = [5, 6, 8, 9, 10]
    print(solution2(a, b))
