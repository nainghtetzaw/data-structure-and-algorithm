class MyLinkedList:
    def __init__(self, val: int = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

    def length(self) -> int:
        counter = 0
        pointer = self.next

        while pointer:
            pointer = pointer.next
            counter += 1

        return counter

    def get(self, index: int) -> int:
        currentIndex = 0
        pointer = self.next
        result = -1

        while pointer:
            if currentIndex == index:
                result = pointer.val
                break
            pointer = pointer.next
            currentIndex += 1

        return result
            

    def addAtHead(self, val: int) -> None:
        node = MyLinkedList(val)
        node.next = self.next
        node.prev = self
        self.next = node
        
        if self.next.next:
            self.next.next.prev = node
            
        self.printAll("addAtHead")


    def addAtTail(self, val: int) -> None:
        initial = self.next
        tail = initial

        if not tail:
            self.addAtHead(val)
            return

        while tail:
            if not tail.next:
                tail.next = MyLinkedList(
                    val = val,
                    prev = tail
                )
                tail = tail.next
                break
            tail = tail.next
        self.printAll("addAtTail")
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length():
            return
        
        currentIndex = 0
        initial = self.next
        pointer = initial

        if index == 0 and not pointer:
            self.addAtHead(val)
            return

        while pointer:
            if currentIndex == index:
                pointer = MyLinkedList(
                    val = val,
                    prev = pointer.prev,
                    next = pointer
                )
                pointer.prev.next = pointer
                pointer.next.prev = pointer
                pointer = pointer.next
                break
            elif not pointer.next and index == self.length():
                self.addAtTail(val)
                break
            pointer = pointer.next
            currentIndex += 1

        self.printAll("addAtIndex")

    def deleteAtIndex(self, index: int) -> None:
        initial = self.next
        pointer = initial
        currentIndex = 0

        while pointer:
            if currentIndex == index:
                if not pointer.prev and not pointer.next:
                    pointer.val = 0
                elif pointer.prev and not pointer.next:
                    node = pointer.prev
                    node.next = None
                    pointer = node
                elif not pointer.prev and pointer.next:
                    node = pointer.next
                    node.prev = None
                    pointer = node
                else:
                    pointer.prev.next = pointer.next
                    pointer.next.prev = pointer.prev
                break

            pointer = pointer.next
            currentIndex += 1

        self.printAll("deleteAtIndex")
        

    def printAll(self, title: object):
        pointer = self.next

        print("---", title, "---")
        while pointer:
            print(pointer.val)
            pointer = pointer.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(0)
obj.addAtIndex(1, 1)
print("get at index 2: ", obj.get(2))
obj.addAtHead(4)
print("get at index 2: ", obj.get(2))
obj.addAtHead(4)
print("get at index 2: ", obj.get(2))
# obj.addAtIndex(0, 10)
# obj.addAtIndex(0, 20)
# obj.addAtIndex(1, 30)
# print("get: ", obj.get(0))
# obj.addAtHead(1)
# obj.addAtHead(2)
# obj.addAtHead(3)
# obj.deleteAtIndex(1)
# print("length: ", obj.length())


# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)