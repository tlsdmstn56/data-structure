class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        old_head = head
        new_head = None
        
        while old_head != None:
            # 1. pop head of old list
            curr = old_head
            old_head = old_head.next
            
            # 2. insert the node into the new list
            curr.next = new_head
            new_head = curr
        
        return new_head
