#Question: easy
#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".
import typing

class Solution:
    def defangIPaddr(self, address: str) -> str:
        #addr = address.split('.')
        #seperator = '[.]'
        return '[.]'.join(address.split('.'))

class Solution2:
    def defangIPaddr(self, address: str) -> str:
        #addr = address.split('.')
        #seperator = '[.]'
        return address.replace('.','[.]')

addr = "255.100.50.0"
result = Solution()
print('Result1:', result.defangIPaddr(addr))

result2 = Solution()
finalresult = result2.defangIPaddr(addr)
print('Result2:', finalresult)

