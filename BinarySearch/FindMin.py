from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1 and nums[0] > nums[-1]:
            temp = nums[0]
            nums.append(temp)
            nums.pop(0)
        
        return nums[0]