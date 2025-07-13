class ListNode:
    def __init__(self, val: str):
        self.val = val
        self.prev = None
        self.next = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode("Null")
        self.right = ListNode("Null")
        self.currentPage = ListNode(homepage)
        self.currentPage.prev = self.left
        self.currentPage.next = self.right
        self.left.next = self.currentPage
        self.right.prev = self.currentPage

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        newNode.next = self.right
        newNode.prev = self.currentPage
        self.right.prev = newNode
        self.currentPage.next = newNode
        self.currentPage = newNode
        

    def back(self, steps: int) -> str:
        pointer = self.currentPage
        result = ""

        while pointer.val != "Null":
            if steps <= 0:
                break
            pointer = pointer.prev
            node = pointer
            result = node.val if node.val != "Null" else node.next.val
            self.currentPage = node if node.val != "Null" else node.next
            steps -= 1    
        
        return result

    def forward(self, steps: int) -> str:
        pointer = self.currentPage
        result = ""

        while pointer.val != "Null":
            if steps <= 0:
                break
            pointer = pointer.next
            node = pointer
            result = node.val if node.val != "Null" else node.prev.val
            self.currentPage = node if node.val != "Null" else node.prev
            steps -= 1

        return result
    

obj = BrowserHistory("initial")
obj.visit("one")
obj.visit("two")
obj.visit("three")
print("steps back: " ,obj.back(7))
print("steps forward: " ,obj.forward(2))
print("steps back: " ,obj.back(1))
print("steps forward: " ,obj.forward(7))