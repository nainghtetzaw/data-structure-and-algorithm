from typing import List

class Solution(object):
    def removeDuplicates(self: int, nums: List[int]):
        leftPointer = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[leftPointer] = nums[r]
                leftPointer += 1

        return leftPointer

        

# Solution.removeDuplicates(0, [1,1,2])
Solution.removeDuplicates(0, [0,0,1,1,1,2,2,3,3,4])