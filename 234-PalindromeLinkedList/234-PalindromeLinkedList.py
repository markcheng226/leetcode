# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals1=[]
        while head:
            vals1.append(head.val)
            head = head.next
        vals2 = list(reversed(vals1))

        if vals1 == vals2:
            return True
        else:
            return False