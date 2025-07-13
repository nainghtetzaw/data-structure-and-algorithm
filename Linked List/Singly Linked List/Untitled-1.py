from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            print("node: ", head.val)
            if (head.next != None):
                self.reverseList(self, head.next)
            else: 
                break
            
        # if (head.next != None):
        #     sortedNode = head.next
        #     sortedNode.next = head
        #     if (head.next.next != None):
        #         sortedNode.next.next = head.next.next
        #     print("sortedNode: ", sortedNode.val)
        #     self.reverseList(self, sortedNode)
        
        return head
    

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Solution.reverseList(Solution, node1)