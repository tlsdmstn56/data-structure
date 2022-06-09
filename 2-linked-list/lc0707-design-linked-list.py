class Node:
    
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        # O(N)
        if index < 0:
            return -1
        curr = self.head
        for _ in range(index):
            if curr == None:
                return -1
            curr = curr.next
        if curr == None:
            return -1
        return curr.value

    def addAtHead(self, val: int) -> None:
        # O(1)
        new_node = Node(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            # linked list is empty
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            prev = self.head
            for _ in range(index-1):
                if prev == None:
                    return -1
                prev = prev.next
            if prev != None:
                # 1. 
                curr = Node(val)
                next_ = prev.next
                # 2. 
                curr.next = next_
                # 3. 
                prev.next = curr
            

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(index-1):
                if prev == None:
                    return -1
                prev = prev.next
            if prev == None or prev.next == None:
                return
            else:
                prev.next = prev.next.next
                
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
