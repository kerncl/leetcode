#Question: Easy
'''
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
'''
from typing import List
import logging
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = math.sqrt(area)
        L = int(mid)
        while area % L:
            L +=1
        W = area // L
        return [max(L,W), min(W,L)]


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    area = 4
    logging.info(f' Position Area {result.constructRectangle(area)}')