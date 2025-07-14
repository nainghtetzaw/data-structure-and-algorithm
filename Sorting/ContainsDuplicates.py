from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) == 1):
            return False
        
        containerSet = set()

        for i in nums:
            if containerSet.__contains__(i):
                return True
            
            containerSet.add(i)
        
        return False