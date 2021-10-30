#Question: easy
#Given an integer number n, return the difference between the product of its digits and the sum of its digits.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumofvalue = 0
        productofvalue = 1
        while n:
            temp = n % 10
            n = int(n/10)
            sumofvalue += temp
            productofvalue *= temp
        diff = productofvalue - sumofvalue
        return int(diff)

class Solution2:
    def subtractProductAndSum(self, n: int) -> int:
        nstr = list(str(n))
        nnumber = [int(string) for string in nstr]
        sumofvalue = 0
        productofvalue = 1
        for value in nnumber:
            sumofvalue += value
            productofvalue *= value
        diff = productofvalue -sumofvalue
        return int(diff)


number = 4421
result = Solution()
diff = result.subtractProductAndSum(number)
print('Result1:', diff)
result2 = Solution2()
diff2 = result2.subtractProductAndSum(number)
print('Result2:', diff2)