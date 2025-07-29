class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        res = ""
        
        for i in range(len(s)):
            res += s[i].lower() if s[i].isalnum() else ""
        
        return res == res[::-1]