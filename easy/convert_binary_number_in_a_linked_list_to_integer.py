#Question: easy
#Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
#Return the decimal value of the number in the linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = 0
        unlinked_list = []
        while head:
            unlinked_list.append(head.val)
            head = head.next
        N = len(unlinked_list) - 1
        for element in unlinked_list:
            if element == 1:
                sum += 2**N
            N -= 1
        return sum

head = [1,0,1]
result = Solution()
integer = result.getDecimalValue(head)

