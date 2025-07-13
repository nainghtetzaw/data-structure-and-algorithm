from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentPointer = 0
        studentCount = len(students)
        sandwichesCount = len(sandwiches)

        while studentCount > 0 and studentPointer <= studentCount:
            print("---   ---")
            print("pointer: ", studentPointer)
            print("students: ", students)
            print("sandwiches: ", sandwiches)
            print("---  END  ---\n")

            if students[0] == sandwiches[0]:
                students.__delitem__(0)
                sandwiches.__delitem__(0)
                studentPointer = 0
                studentCount = len(students)
                sandwichesCount = len(sandwiches)
            else:
                students.append(students[0])
                students.__delitem__(0)
                studentPointer += 1

        return sandwichesCount


print("unableToEatStudent: " ,Solution.countStudents(Solution, [1,1,1,0,0,1], [1,0,0,0,1,1]))