## LeetCode link: https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2

            if isBadVersion(m):
                if isBadVersion(m - 1):
                    r = m - 1
                else:
                    return m
            else:
                l = m + 1
        
        return -1