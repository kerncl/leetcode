#Question: Easy
'''
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.
'''
import logging
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            temp = start
            start = destination
            destination = temp
        return min(sum(distance[start:destination]), sum(distance[index2] for index2 in range(destination-len(distance), start)))


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(level=logging.DEBUG)
    result = Solution()
    distance = [1, 2, 3, 4]
    start = 0
    destination = 1
    logging.info(f'Shortest distance {result.distanceBetweenBusStops(distance, start, destination)}')
