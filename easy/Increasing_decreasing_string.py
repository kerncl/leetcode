#Question: easy
#Given a string s. You should re-order the string using the following algorithm:
#Pick the smallest character from s and append it to the result.
#Pick the smallest character from s which is greater than the last appended character to the result and append it.
#Repeat step 2 until you cannot pick more characters.
#Pick the largest character from s and append it to the result.
#Pick the largest character from s which is smaller than the last appended character to the result and append it.
#Repeat step 5 until you cannot pick more characters.
#Repeat the steps from 1 to 6 until you pick all characters from s.
#In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
#Return the result string after sorting s with this algorithm.
import string

class Solution:
    def sortString(self, s: str) -> str:
        char_counts = dict()
        for char_index in range(len(s)):
            character = s[char_index]
            if character in char_counts:
                char_counts[character] = char_counts[character] + 1
            else:
                char_counts[character] = 1

        move_happened = True
        ascending = True
        ret_list = list()
        alphabet = list(string.ascii_lowercase)

        while move_happened:
            move_happened = False

            if ascending:
                ascending = False
                for character in alphabet:
                    if character in char_counts and char_counts[character] > 0:
                        ret_list.append(character)
                        char_counts[character] = char_counts[character] - 1
                        move_happened = True

            else:
                ascending = True
                for char_index in range(len(alphabet) - 1, -1, -1):
                    character = alphabet[char_index]

                    if character in char_counts and char_counts[character] > 0:
                        ret_list.append(character)
                        char_counts[character] = char_counts[character] - 1
                        move_happened = True

        return "".join(ret_list)


s = "aaaabbbbcccc"
result = Solution()
string = result.sortString(s)
print('Sorted string:', string)