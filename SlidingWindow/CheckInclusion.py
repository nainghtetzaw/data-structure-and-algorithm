class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        minS = min(s1, s2)

        for l in range(len(max(s1, s2))):
            r = l + len(minS)

            if r >= len(max(s1, s2)):
                break
            
            if sorted(minS) == sorted(max(s1, s2)[l:r]):
                return True

        return False