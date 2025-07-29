from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        j = i + 1
        
        while j < len(nums):
            for z in range(1, len(nums)):
                if z != j:
                    if nums[i] + nums[j] + nums[z] == 0:
                        if sorted(list([nums[i], nums[j], nums[z]])) not in res:
                            res.append(sorted(list([nums[i], nums[j], nums[z]])))
            
            j += 1
        
        return res
    
    
result = Solution.threeSum(Solution, [-1,0,1,2,-1,-4])

for i in result:
    print("\n")
    print("[")
    for j in i:
        print(j)
    print("]")