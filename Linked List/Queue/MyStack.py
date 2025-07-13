class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class MyStack:

    def __init__(self):
        self.stack = ListNode(-1)

    def push(self, x: int) -> None:
        node = ListNode(x)
        node.right = self.stack
        node.left = self.stack.left
        if self.stack.left:
            self.stack.left.right = node
        self.stack.left = node

    def pop(self) -> int:
        if (self.stack.left):
            result = self.stack.left.val
            self.stack.left = self.stack.left.left
            if self.stack.left:
                self.stack.left.right = self.stack
            return result
        return -1

    def top(self) -> int:
        if (self.stack.left):
            return self.stack.left.val
        return -1

    def empty(self) -> bool:
        return False if self.stack.left else True
    
myStack = MyStack()
myStack.push(1)
# myStack.push(2)
print("top: ", myStack.top())
print("pop: ", myStack.pop())
print("isEmpty: ", myStack.empty())