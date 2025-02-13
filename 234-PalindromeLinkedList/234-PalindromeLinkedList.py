# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val1 = []

        while head:
            val1.append(head.val)
            head = head.next
        
        val2 = list(reversed(val1))
        if val1 == val2:
            return True
        else:
            return False