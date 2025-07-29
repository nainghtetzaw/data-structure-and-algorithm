from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums

        res = {}

        for i in nums:
            res[i] = 1 if res.get(i) == None else res[i] + 1

        res = dict(sorted(res.items(),key =  lambda item: item[1]))
        for i in range(len(res) - k):
            del res[next(iter(res))]
        
        return list(res.keys())
    

result = Solution.topKFrequent(Solution, [1,1,1,2,2,3], 2)

for i in result:
    print(i)