class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        longestLen, l, r = 0, 0, 1

        while r < len(s):
            if s[r] in s[l:r]:
                longestLen = max(longestLen, len(s[l:r]))
                l += 1
                r = l + 1
            else:
                r += 1

            if r == len(s):
                longestLen = max(longestLen, len(s[l:r]))

        return longestLen