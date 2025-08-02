from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        i, j, z = 0, 1, len(nums) - 1
        
        nums.sort()
        
        while i < len(nums):
            while j < z:
                if j != i and z != i and j != z:
                    threeSum = nums[i] + nums[j] + nums[z]
                    
                    if threeSum > 0:
                        z -= 1
                    elif threeSum < 0:
                        j += 1
                    else:
                        res.append([nums[i], nums[j], nums[z]])
                        j += 1
                        z -= 1
                elif j == i:
                    j += 1
                elif z == i:
                    z -= 1
                        
            i += 1
            j = 0
            z = len(nums) - 1
        
        return list(dict.fromkeys(res))
    
    
result = Solution.threeSum(Solution, [-1,0,1,2,-1,-4])

print(result)