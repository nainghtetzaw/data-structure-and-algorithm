class MinStack:
    def __init__(self):    
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        currentMin = self.minStack[-1] if self.minStack else val
        self.minStack.append(val if val < currentMin else currentMin)
        self.stack.append(val)
    
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else 0

    def getMin(self) -> int:
        return self.minStack[-1]


obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
obj.pop()
obj.pop()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)