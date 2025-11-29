from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        hm = {i : [] for i in range(numCourses)}

        for i, a in prerequisites:
            hm[i].append(a)

        visited = set()

        def dfs(key):
            if key in visited:
                return False
            if not hm[key]:
                return True

            visited.add(key)
            for j in hm[key]:
                if not dfs(j):
                    return False
            visited.remove(key)
            hm[key] = []
                
            return True

        for k in hm.keys():
            if not dfs(k):
                return False

        return True