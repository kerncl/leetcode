# Question: Easy
'''
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.
'''
from typing import List
import logging

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        stack = []
        third_list = []
        for word in text.split(' '):
            if len(stack) == 2:
                third_list.append(word)
                stack.clear()
            if word == first:
                stack.clear()
                stack.append(word)
            elif stack != []:
                if word == second:
                    stack.append(word)
                else:
                    stack.clear()
        return third_list


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.INFO)
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    text2 = "we will we will rock you"
    first2 = "we"
    second2 = "will"
    text3 = "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"
    first3 = "kcyxdfnoa"
    second3 = "jkypmsxd"
    text4 = "obo jvezipre obo jnvavldde jvezipre jvezipre jnvavldde jvezipre jvezipre jvezipre y jnvavldde jnvavldde obo jnvavldde jnvavldde obo jnvavldde jnvavldde jvezipre"
    first4 = "jnvavldde"
    second4 = "y"
    result = Solution()
    logging.info(f'Third Ans: {result.findOcurrences(text=text4, first=first4, second=second4)}')
