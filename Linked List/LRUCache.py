class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {} # {key : Pair(value : timestamp)}
        self.timestamp = 0
    
    def getLeastRecentKey(self) -> int:
        return min(self.hm, key = lambda k: self.hm[k][1])

    def getTimestamp(self) -> int:
        self.timestamp += 1
        return self.timestamp

    def get(self, key: int) -> int:
        if key in self.hm:
            self.hm[key] = (self.hm[key][0], self.getTimestamp())
            return self.hm[key][0]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key] = (value, self.getTimestamp())
            return
        
        if len(self.hm) == self.capacity:
            del self.hm[self.getLeastRecentKey()]
        
        self.hm[key] = (value, self.getTimestamp())
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)