from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        bucket = [0,0,0]
        for i in nums:
            bucket[i] += 1
        
        pointer = 0
        for i in range(0, len(bucket)):
            for j in range(1, bucket[i] + 1):
                nums[pointer] = i
                pointer += 1

# arr = [2, 0, 2, 1, 1, 0]
arr = [2, 0, 1]
Solution.sortColors(Solution, arr)