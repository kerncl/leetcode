"""
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""
def max_sum_list(a:list, reverse=False):
    sum = 0
    cumulative_list = []
    if reverse:
        a.reverse()
    for _ in a[1:-1]:
        sum += _
        if sum > 0:
            cumulative_list.append(sum)
        else:
            sum = 0
            if cumulative_list:
                cumulative_list.append(0)

    if reverse:
        cumulative_list.reverse()
    return cumulative_list

def solution(a):
    # Kandas
    forwards_sum = max_sum_list(a.copy())
    reverse_sum = max_sum_list(a.copy(), reverse=True)

    min_len = min(len(forwards_sum), len(reverse_sum))

    sum_list = []
    for i in range(min_len):
        if i <= 0:
            forward_v = 0
        else:
            forward_v = forwards_sum[i-1]
        if (i+1) >= min_len:
            backward_v = 0
        else:
            backward_v = reverse_sum[i+1]

        sum_list.append(forward_v+backward_v)

    return max(sum_list)


if __name__ == '__main__':
    a = [3,2,6,-1,4,5,-1,2]
    print(f'{a}: Max Slice Sum: {solution(a)}')
