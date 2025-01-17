# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        exist = set()
        cur = head
        while cur:
            if cur in exist:
                return True
            exist.add(cur)
            cur = cur.next
        return False