def fibonacci_(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_(n-1) + fibonacci_(n-2)


if __name__ == '__main__':
    for _ in range(10):
        print(f"{fibonacci_(_)}")
