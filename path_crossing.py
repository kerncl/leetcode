#Question: Easy
'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.
'''
import logging
from collections import Counter

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        ans = [(x,y)]
        # dict_operator = {
        #     'N':lambda x,y: y+1,
        #     'S': lambda x,y: y-1,
        #     'E': lambda x,y: x+1,
        #     'W': lambda x,y: x-1
        # }
        # for dir in path:
        #     y = dict_operator[dir](x,y)
        for direction in path:
            if direction == 'N':
                y +=1
            elif direction == 'S':
                y -=1
            elif direction == 'E':
                x +=1
            elif direction == 'W':
                x -=1
            if (x,y) in ans:
                return True
            ans.append((x,y))
        return False

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    path = "NESWW"
    path2 = 'NES'
    path3 = "NNSWWEWSSESSWENNW"
    result = Solution()
    logging.info(f'Does it have interception: {result.isPathCrossing(path3)}')