from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        clone = set()
        for i in nums:
            if i in clone:
                return i
            
            clone.add(i)
        
        return -1