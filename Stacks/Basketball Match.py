from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreList: List[int] = []
        
        for i in operations:
            if i.lower() == "c":
                scoreList.pop()
            elif i.lower() == "d":
                scoreList.append(scoreList[-1] * 2)
            elif i.lower() == "+":
                scoreList.append(scoreList[-1] + scoreList[-2])
            else:
                scoreList.append(int(i))

        print(sum(scoreList))
        return sum(scoreList)
    

# Solution.calPoints(Solution, ["5","2","C","D","+"])
Solution.calPoints(Solution, ["5","-2","4","C","D","9","+","+"])
# Solution.calPoints(Solution, ["1","C"])