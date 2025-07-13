from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []

        for i in range(0, len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                temp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = temp
                j -= 1
            
            result.append(pairs[:])

        return result
    
pairs = [Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]
expected = [[Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")], 
 [Pair(2, "banana"), Pair(5, "apple"), Pair(9, "cherry")], 
 [Pair(2, "banana"), Pair(5, "apple"), Pair(9, "cherry")]]

# assert expected == Solution.insertionSort(Solution, pairs)
for list in Solution.insertionSort(Solution, []):
    for pair in list:
        print("key: ", pair.key, "value: ", pair.value, end = "\n")

    print("--- ---")