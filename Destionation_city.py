#Question: easy
#You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
#It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        front = set()
        back = set()
        for start, end in paths:
            front.add(start)
            back.discard(start)
            if end not in front:
                back.add(end)
        return back.pop()


#paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
paths = [["B", "C"], ["D", "B"], ["C", "A"]]
result = Solution()
city = result.destCity(paths)
print('Final destination:', city)