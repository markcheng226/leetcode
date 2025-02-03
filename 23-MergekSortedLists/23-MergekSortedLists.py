class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]

        while len(lists) >1:
            res = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i +1 < len(lists) else None
                res.append(self.mergeLists(l1,l2))
            lists = res
        return lists[0]

    


    def mergeLists(self,l1,l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail= tail.next
        
        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next