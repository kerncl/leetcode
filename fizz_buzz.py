#Question: Easy
"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""
import logging
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output_list = []
        for index in range(1, n+1):
            if not index % 15:
                output_list.append('FizzBuzz')
            elif not index % 3:
                output_list.append('FizzBuzz')
            elif not index % 5:
                output_list.append('Buzz')
            else:
                output_list.append(str(index))
        return output_list


if __name__ == "__main__":
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    n = 15
    result = Solution()
    logging.info(f'Output list: {result.fizzBuzz(n)}')