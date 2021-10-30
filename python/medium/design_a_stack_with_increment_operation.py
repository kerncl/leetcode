"""
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.
"""
import logging
import sys
from queue import Queue


class CustomStack:

    def __init__(self, maxSize: int):
        # self.stack = Queue(maxsize=maxSize)
        self.stack = []
        self.maxsize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxsize:
            self.stack.append(x)
        # try:
        #     self.stack.put_nowait(x)
        # except:
        #     pass
        #     # raise error if full

    def pop(self) -> int:
        try:
            return self.stack.pop()
        except:
            return -1
        # if self.stack.empty():
        #     return -1
        # return self.stack.get()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

    def __repr__(self):
        return str(self.stack)


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    format = '%(asctime)s [%(levelname)s]: %(message)s'

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setLevel(logging.INFO)
    stream.setFormatter(logging.Formatter(format))

    log.addHandler(stream)

    mystack = CustomStack(3)

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)
