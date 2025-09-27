class TimeMap:
    def __init__(self):
        self.hm = {} # {key, [(value, timestamp)...]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hm.get(key, [])

        if values and values[-1][1] <= timestamp:
            return values[-1][0]

        l, r = 0, len(values) - 1
        while l <= r:
            m = (r + l) // 2
            if values[m][1] <= timestamp:
                if values[m + 1][1] <= timestamp:
                    l = m + 1
                else:
                    return values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                return values[m][0]
            
        return ""