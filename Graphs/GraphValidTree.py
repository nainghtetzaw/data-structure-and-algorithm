from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        hm = {i : [] for i in range(n)}
        
        for i in edges:
            hm[i[0]].append(i[1])
            hm[i[1]].append(i[0])

        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in hm[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False
            return True
                
        return dfs(0, -1) and len(visited) == n