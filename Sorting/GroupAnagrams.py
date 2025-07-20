from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        result = {}

        for i in strs:
            sortedStr = "".join(sorted(i))

            if result.get(sortedStr) != None:
                result[sortedStr].append(i)
            else:
                result[sortedStr] = [i]

        return list(result.values())
    
result = Solution.groupAnagrams(Solution, ["eat","tea","tan","ate","nat","bat"])

for i in result:
    print(i)
