class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        l, r = 0, len(s) - 1
        
        while l <= r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                
                l += 1
                r -= 1
        
        
        return True
    
result = Solution.isPalindrome(Solution, "Was it a car or a cat I saw?")
print(result)