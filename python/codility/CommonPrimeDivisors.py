"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A and B is an integer within the range [1..2,147,483,647].
"""

def get_primes(n):
    primes = []
    for i in range(1, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

def get_factors():
    pass

def solution(a, b):
    max_i = max(a + b)
    primes = get_primes(max_i)
    count = 0
    for i in range(len(a)):
        a_v = a[i]
        b_v = b[i]
        max_v = max(a_v, b_v)
        for prime in (_ for _ in primes if _ <= max_v):
            # if both doesnt match go to next prime
            # a yes, b no --> break
            # a no, b yes --> break
            # a no, b no --> continue
            # a yes, b yes --> continue
            # prime not occurs in both --> continue
            if any([a[i] % prime, b[i] % prime]) and not all([a[i] % prime, b[i] % prime]): # either one is divisible by prime
                break
        else:
            count += 1
    return count

if __name__ == '__main__':
    a = [15, 10, 3]
    b = [75, 30, 5]
    # print(f'Primes: {get_primes(75)}')
    print(f'Number of positions: {solution(a, b)}')
