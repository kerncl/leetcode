#Question: Easy
"""
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.
"""
from typing import List
import logging


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        candidate = [0]*num_people
        index = 0
        candie = 1
        while candies > 0:
            candidate[index] = candie +candidate [index]
            candie +=1
            candies -= candie
            index += 1
            if index == num_people:
                index = 0
            if candies <= 0:
                candidate[index] += candies + candie - 1
                break

        return candidate



if __name__ == "__main__":
    format ="%(asctime)s %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    candies = 7
    num_people = 4
    candies2 = 10
    num_people2 = 3
    candies3 = 80
    num_people3 = 4
    candies4 = 90
    num_people4 = 4
    result = Solution()
    logging.info(f'Candies distribute {result.distributeCandies(candies4,num_people4)}')