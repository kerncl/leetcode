#Question: Easy
'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
'''
import logging


class Solution:
    def maxPower(self, s: str) -> int:
        count_list = []
        temp_value = None
        count = 0
        for index, value in enumerate(s):
            if temp_value is None:
                temp_value = value
            if temp_value != value:
                count_list.append(count)
                temp_value = value
                count = 1
                continue
            count += 1
        count_list.append(count)
        return max(count_list)

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    s = "leetcode"
    s2 = "triplepillooooow"
    s3 = "hooraaaaaaaaaaay"
    s4 = 'j'
    s5 = 'cc'
    logging.info(f'The max power {result.maxPower(s4)}')