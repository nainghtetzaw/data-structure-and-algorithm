from typing import List

class LinkNode:
    def __init__(self, val: int, next_node = None) -> None:
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = LinkNode(-1, None)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        currentNode: LinkNode = self.head

        while (currentNode.next):
            if (i < index):
                currentNode = currentNode.next
                i += 1
            else:
                return currentNode.val

        return -1

    def insertHead(self, val: int) -> None:
        newHead = LinkNode(val)
        newHead.next = self.head.next
        self.head.next = newHead
        if self.head.next:
            self.tail = self.head



    def insertTail(self, val: int) -> None:
        newTail = LinkNode(val)
        self.tail.next = newTail 
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        currentNode = self.head

        while (i < index and currentNode):
            currentNode = currentNode.next
            i += 1

        if (currentNode and currentNode.next):
            if (currentNode.next == self.tail):
                self.tail = currentNode
            currentNode.next = currentNode.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        result = []
        currentNode = self.head

        while (currentNode.next):
            result.append(currentNode.val)
            currentNode = currentNode.next
        return result
    

linkedListInstance = LinkedList()
linkedListInstance.insertHead(6)
print(linkedListInstance.get(0))
linkedListInstance.insertHead(1)
linkedListInstance.insertTail(3)
# print(linkedListInstance.remove(3))

print(linkedListInstance.getValues())