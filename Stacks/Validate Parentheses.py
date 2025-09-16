class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        brackets = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i in brackets.values():
                stack.append(i)
                continue
            
            if not stack:
                return False
            
            if brackets[i] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return True if len(stack) == 0 else False

print(Solution.isValid(Solution, "({[]})"))
print(Solution.isValid(Solution, "(){}[]"))
print(Solution.isValid(Solution, "()"))
print(Solution.isValid(Solution, "(]"))