from collections import Counter

def solution(S):
    max = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S)+1):
            if all([not v%2 for v in Counter(S[i:j]).values()]):
                if len(S[i:j]) > max:
                    max = len(S[i:j])
    return max


if __name__ == "__main__":
    tests = [
        # ('bdaaadadb', 6),
        #      ('abacb', 0),
             ('zthtzh', 6)]
    for i, (s, ans) in enumerate(tests,1):
        myans = solution(s)
        assert myans == ans, f"{i} S:{s} expected: {ans} got: {myans}"
