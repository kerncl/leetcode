# Question: Easy
'''
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.
'''
from typing import List
from pprint import pprint
import logging


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        tic_tock = [['', '', ''],
                    ['', '', ''],
                    ['', '', '']]
        for i in range(0, len(moves)):
            if i % 2:
                tic_tock[moves[i][0]][moves[i][1]] = 'o'
            else:
                tic_tock[moves[i][0]][moves[i][1]] = 'x'

        # Check for vertical and horizontal
        for column, row in enumerate(tic_tock):
            if row.count('x') == 3:
                return 'A'
            if row.count('o') == 3:
                return 'B'
            if tic_tock[0][column] == tic_tock[1][column] == tic_tock[2][column]:
                if tic_tock[0][column] == 'x':
                    return 'A'
                elif tic_tock[0][column] == 'o':
                    return 'B'

        # check for cross
        mid = tic_tock[1][1]
        if tic_tock[0][0] == tic_tock[2][2] == tic_tock[1][1] or tic_tock[2][0] == tic_tock[1][1] == tic_tock[0][2]:
            if tic_tock[1][1] == 'x':
                return 'A'
            elif tic_tock[1][1] == 'o':
                return 'B'

        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    moves2 = [[0,0],[1,1]]
    logging.info(f'{result.tictactoe(moves2)}')
