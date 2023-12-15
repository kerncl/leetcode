def solution(R,V):
    if len(R) == 0:
        return [0,0]
    if len(R) == 1:
        return [V[0],0] if R == 'B' else [0,V[0]]
    # final either 1 is 0
    init_a = 0  # assume starting is 0 for both
    init_b = 0
    curr_a = 0
    curr_b = 0
    for r, v in zip(R, V):
        if r == 'A':
            curr_a += v
            curr_b -= v
        else:
            curr_a -= v
            curr_b += v

        # value checking
        if curr_a < 0:
            topup = abs(curr_a)
            init_a += topup
            curr_a = 0
        if curr_b < 0:
            topup = abs(curr_b)
            init_b += topup
            curr_b = 0


    return [init_a, init_b]


if __name__ == "__main__":
    tests = [('BAABA', [2, 4, 1, 1, 2], [2,4]),
             ('ABAB', [10, 5, 10, 15], [0,15]),
             ('B', [100], [100,0]),]
    for R, V, ans in tests:
        myans = solution(R, V)
        assert myans == ans, f"R:{R}, V:{V} expected: {ans} got: {myans}"
