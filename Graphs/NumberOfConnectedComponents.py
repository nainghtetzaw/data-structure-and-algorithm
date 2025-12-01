from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        hm = {i : [] for i in range(n)}
        visited = set()

        for i, a in edges:
            hm[i].append(a)
            hm[a].append(i)

        def dfs(i):
            visited.add(i)
            for j in hm[i]:
                if j in visited:
                    continue
                dfs(j)
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count