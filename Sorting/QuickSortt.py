from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(
            self,
            pairs: List[Pair]
    ) -> List[Pair]:
        return self.sort(self, pairs, 0, len(pairs) - 1)

    def sort(
            self,
            pairs: List[Pair],
            start: int,
            end: int
    ) -> List[Pair] :
        if ((end - start) + 1 <= 1):
            return pairs

        pivot = end
        left = start

        for i in range(start, end):
            if (pairs[i][0] < pairs[pivot][0]):
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1

        temp = pairs[pivot]
        pairs[pivot] = pairs[left]
        pairs[left] = temp

        self.sort(self, pairs, start, left - 1)
        self.sort(self, pairs, left + 1, end)

        return pairs
    
pairs = [(3, "cat"), (2, "dog"), (3, "bird"), (5, "apple"), (9, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
# pairs = [(5, "apple"), (9, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
result = Solution.quickSort(Solution, pairs)

for i in result:
    print("key: ", i[0], "value: ", i[1])