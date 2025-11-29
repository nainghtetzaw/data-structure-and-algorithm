from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        hm = {i : [] for i in range(numCourses)}
        seen = set()

        for i, a in prerequisites:
            hm[i].append(a)

        def dfs(key, visited):
            if key in visited:
                return False

            visited.append(key)
            for j in hm[key]:
                if j in seen:
                    continue
                if not dfs(j, visited):
                    return False

            visited.pop()
            seen.add(key)
                
            return True

        for k in hm.keys():
            if len(seen) == numCourses:
                break
            if not dfs(k, []):
                return False

        return True