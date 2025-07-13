# LeetCode link: https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1497152674/
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l + r) // 2

            if guess(m) < 0:
                r = m - 1
            elif guess(m) > 0:
                l = m + 1
            else:
                return m
            
        return -1