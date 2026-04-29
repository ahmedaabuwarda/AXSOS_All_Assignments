class MyHashMap:

    def __init__(self, length=8):
        self.length = length
        self.table = [[],[],[],[],[],[],[],[]]

    def _hash(self, key):
        return key % self.length

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        # Manually loop through the inner list
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                return self.table[idx][i][1]
        return -1
        

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                # Remove using the index directly
                del self.table[idx][i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
