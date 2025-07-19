from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i, n in enumerate(nums):
            diff = target - n

            if hm.get(diff, None) != None:
                return [hm[diff], i]
            
            hm[n] = i

        return []
    
print(Solution.twoSum(Solution, [0, 40, 3, 0], 0))