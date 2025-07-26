from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return len(nums)
        
        res = []
        prev = None
        counter = 1
        
        for i in sorted(nums):
            if prev != None and i != prev:
                if i - prev == 1:
                    counter += 1
                else:
                    counter = 1
                
            prev = i
            res.append(counter)
        
        return max(res)
        
print(Solution.longestConsecutive(Solution, [100,4,200,1,3,2]))