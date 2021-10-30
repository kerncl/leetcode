#Question: Easy
'''
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.
'''


class Solution:
    def toGoatLatin(self, S: str) -> str:
        list_str = S.split(' ')
        s = ''
        for index, word in enumerate(list_str):
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                s += ''.join('{word}ma{a} ' .format(word=word, a='a'*(index+1)))
            else:
                s += ''.join('{word}{alp}ma{a} ' .format(word=word[1:], alp=word[0], a='a'*(index+1)))
        return s.strip()


s = "I speak Goat Latin"
result = Solution()
print(f'{s} --> {result.toGoatLatin(s)}')
