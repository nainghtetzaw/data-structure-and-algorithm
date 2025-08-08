# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(
            self, 
            lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.mergeSort(self, lists, 0, len(lists) - 1)
    
    def mergeSort(
            self, 
            lists: List[Optional[ListNode]],
            start: int,
            end: int
    ) -> Optional[ListNode]:
        if (end - start + 1 <= 1):
            result = lists[start]
            return result
        
        medium = start + (end - start) // 2
        left = self.mergeSort(self, lists, start = start, end = medium)
        right = self.mergeSort(self, lists, start = medium + 1, end =  end)

        return self.merge(self, left, right)
    
    def merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        resultTail = result

        while (left and right):
            if right.val < left.val:
                resultTail.next = right
                right = right.next
            elif left.val <= right.val:
                resultTail.next = left
                left = left.next

            resultTail = resultTail.next
        
        if left:
            resultTail.next = left
        else:
            resultTail.next = right

        return result.next

# Create small linked lists
list1 = ListNode(val=3, next=ListNode(val=7))
list2 = ListNode(val=1, next=ListNode(val=4))
list3 = ListNode(val=5, next=ListNode(val=8))
list4 = ListNode(val=2, next=ListNode(val=6))
list5 = ListNode(val=9, next=ListNode(val=10))

# Add the head nodes of these linked lists to a list
linked_lists = [list1, list2, list3, list4, list5]
result = Solution.mergeKLists(Solution, linked_lists)
resultTail = result

while (resultTail):
    print(resultTail.val)
    resultTail = resultTail.next