import string


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        if len(s1) == len(s2):
            return sorted(s1) == sorted(s2)
        
        minS = min(s1, s2, key = len)
        maxS = max(s1, s2, key = len)

        for l in range(len(maxS)):
            r = l + len(minS)

            if r > len(maxS):
                break
            
            if sorted(minS) == sorted(maxS[l:r]):
                return True

        return False
