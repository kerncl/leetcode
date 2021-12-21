"""
You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
"""
import functools
import logging
from typing import List
from collections import defaultdict

format = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger('mylog')
log.setLevel(level=logging.INFO)

stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
stream.setFormatter(format)
log.addHandler(stream)


class DetectSquares:

    def __init__(self):
        # self.coor = []
        self.y_coor = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # self.coor.append(point)
        self.y_coor[point[1]] += 1

    def count(self, point: List[int]) -> int:
        if any(i<0 for i in point):
            return 0

        if self.y_coor.get(point[1], 0):
            # return functools.reduce(lambda x1,x2: x1*(x2-1),self.y_coor.values())
            return functools.reduce(lambda x1,x2: x1*x2, map(lambda x: x-1 if x>1 else 1, self.y_coor.values()))

        return 0

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)


if __name__ == '__main__':
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    assert detectSquares.count([11, 10]) == 1, log.error(
        f'Expected return 1, but received: {detectSquares.count([11, 10])}')
    # return 1.    You can choose:
    # - The first, second, and third points
    assert detectSquares.count([14, 8]) == 0, log.error(
        f'Expected return 1, but received: {detectSquares.count([14, 8])}')
    # return 0. The query point cannot form a square with any points in the data structure.
    detectSquares.add([11, 2])  # Adding duplicate points is allowed.
    assert detectSquares.count([11, 10]) == 2, log.error(
        f'Expected return 2, but received: {detectSquares.count([11, 10])}')
    # return 2. You can choose: - The first, second, and third points
    # - The first, third, and fourth points

    cmds = ["add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count"]
    params = [[[419,351]],[[798,351]],[[798,730]],[[419,730]],[[998,1]],[[0,999]],[[998,999]],[[0,1]],[[226,561]],[[269,561]],[[226,604]],[[269,604]],[[200,274]],[[200,793]],[[719,793]],[[719,274]],[[995,99]],[[146,948]],[[146,99]],[[995,948]],[[420,16]],[[962,558]],[[420,558]],[[962,16]],[[217,833]],[[945,105]],[[217,105]],[[945,833]],[[26,977]],[[26,7]],[[996,7]],[[996,977]],[[96,38]],[[96,483]],[[541,483]],[[541,38]],[[38,924]],[[961,1]],[[961,924]],[[38,1]],[[438,609]],[[818,609]],[[818,229]],[[438,229]]]
    anss = [None, None, None, 1, None, None, None, 1, None, None, None, 1, None, None, None, 1, None,
           None, None, 1,
           None, None, None, 1, None, None, None, 1, None, None, None, 1, None, None, None, 1, None, None,
           None, 1, None,
           None, None, 1]
    detectSquares1 = DetectSquares()
    for cmd,param,expected in zip(cmds, params, anss):
        method = getattr(detectSquares1, cmd)
        ans = method(param[0])
        assert expected == ans, log.error(f'Expected ans: {expected}, but received: {ans}')


    cmds2 = ["add","add","add","add","add","add","count","add","add","count","add","count","add","add","add","add","add","add","add","add","add","add","add","count","add","add","add","add","count","add","count","add","add","count","add","add","add","add","add","count","add","count","count","add","add","add","add","add","count","count","count","count","count","add","count","add","count","add","add","count","add","count","count","add","count","count","add","count","count","add","add","add","add","add","count","count","add","add","add","count","add","add","count","add","count","count","add","count","add","count","add","add","add","count","add","add","add","count","count","count","add","count","add","add","add","add","add","count","count"]
    params2 = [[[544,463]],[[740,114]],[[202,206]],[[407,643]],[[872,530]],[[411,811]],[[902,310]],[[478,300]],[[569,269]],[[392,825]],[[421,397]],[[234,720]],[[463,755]],[[951,125]],[[577,441]],[[322,901]],[[176,664]],[[225,954]],[[307,574]],[[434,229]],[[749,187]],[[619,629]],[[974,689]],[[142,210]],[[989,525]],[[75,737]],[[455,364]],[[319,672]],[[647,1000]],[[112,446]],[[326,907]],[[104,75]],[[551,901]],[[673,604]],[[362,570]],[[703,325]],[[857,334]],[[586,838]],[[604,461]],[[593,797]],[[421,702]],[[738,734]],[[730,915]],[[61,187]],[[679,448]],[[720,475]],[[973,734]],[[857,797]],[[849,288]],[[181,388]],[[351,398]],[[135,561]],[[557,338]],[[860,966]],[[489,227]],[[852,475]],[[66,223]],[[602,821]],[[420,883]],[[684,620]],[[816,963]],[[390,947]],[[896,11]],[[109,347]],[[571,342]],[[284,864]],[[343,221]],[[636,352]],[[352,140]],[[564,591]],[[124,303]],[[272,607]],[[664,167]],[[694,188]],[[301,403]],[[70,474]],[[258,276]],[[580,211]],[[853,386]],[[19,854]],[[70,913]],[[755,254]],[[875,897]],[[295,471]],[[33,809]],[[674,604]],[[183,684]],[[951,564]],[[30,229]],[[479,477]],[[229,936]],[[38,531]],[[414,715]],[[950,231]],[[647,636]],[[956,149]],[[585,178]],[[705,984]],[[970,632]],[[650,676]],[[156,640]],[[404,913]],[[155,597]],[[842,810]],[[380,692]],[[731,188]],[[223,606]],[[764,71]],[[763,239]]]
    ans2 = [None, None, None, None, None, None, None, 0, None, None, 0, None, 0, None, None, None, None,
            None, None, None, None, None, None, None, 0, None, None, None, None, 0, None, 0, None, None, 0,
            None, None, None, None, None, 0, None, 0, 0, None, None, None, None, None, 0, 0, 0, 0, 0, None, 0,
            None, 0, None, None, 0, None, 0, 0, None, 0, 0, None, 0, 0, None, None, None, None, None, 0, 0,
            None, None, None, 0, None, None, 0, None, 0, 0, None, 0, None, 0, None, None, None, 0, None,
            None, None, 0, 0, 0, None, 0, None, None, None, None, None, 0, 0]
    detectSquares2 = DetectSquares()
    for cmd,param2,expected in zip(cmds2, params2, ans2):
        method = getattr(detectSquares2, cmd)
        ans = method(param2[0])
        assert expected == ans, log.error(f'Expected ans: {expected}, but received: {ans}')