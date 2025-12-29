class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            subStr = s[0:i + 1]

            if self.isPalindrome(subStr):
                res = max(res, subStr, key = len)

            for j in range(len(subStr)):
                if self.isPalindrome(subStr[j:]):
                    res = max(res, subStr[j:], key = len)

        return res