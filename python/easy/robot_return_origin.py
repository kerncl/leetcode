#Question: easy
#There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
#The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
#Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
import time

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical = 0
        horizontal = 0
        for movement in moves:
            if movement == 'U':
                vertical += 1
            elif movement == 'D':
                vertical -= 1
            elif movement == 'R':
                horizontal += 1
            elif movement == 'L':
                horizontal -= 1
        if vertical == 0 and horizontal ==0:
            origin = True
        else:
            origin = False
        return origin

class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


move = 'LL'
result = Solution()
start1 = time.perf_counter_ns()
origin = result.judgeCircle(move)
time1 = time.perf_counter_ns() - start1
print('1 Robot move back origin: ', origin)
print('Total use time: {sec} ns' .format(sec=time1))
result2 = Solution2()
start2 = time.perf_counter_ns()
origin2 = result2.judgeCircle(move)
time2 = time.perf_counter_ns() - start2
print('2 Robot move back origin: ', origin2)
print('Total use time: {sec} ns' .format(sec=time2))
