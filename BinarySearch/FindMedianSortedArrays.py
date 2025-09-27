import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        m = (len(nums) - 1) / 2
        if m == math.ceil(m):
            return nums[math.ceil(m)]
        
        return (nums[math.floor(m)] + nums[math.ceil(m)]) / 2