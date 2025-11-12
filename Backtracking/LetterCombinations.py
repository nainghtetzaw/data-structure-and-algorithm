from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hm = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"], 
            '4': ["g", "h", "i"], 
            '5': ["j", "k", "l"], 
            '6': ["m", "n", "o"], 
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        res = []

        def dfs(cur, s):
            if cur >= len(digits):
                res.append("".join(s))
                return
            
            for i in hm[digits[cur]]:
                s.append(i)
                dfs(cur + 1, s)
                s.pop()
        
        dfs(0, [])
        return res