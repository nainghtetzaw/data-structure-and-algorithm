from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        hm = {i : [] for i in range(numCourses)}

        for c, p in prerequisites:
            hm[c].append(p)
        
        res = []
        visited, cycle = set(), set()
        def dfs(c) -> bool:
            if c in cycle: 
                return False
            if c in visited:
                return True

            cycle.add(c)
            for i in hm[c]:
                if not dfs(i):
                    return False

            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res