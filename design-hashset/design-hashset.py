class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hashset = [None] * self.size
        
    def hash_function(self,key):
        return key % self.size

    def add(self, key: int) -> None:
        hashed_value = self.hash_function(key)
        if self.hashset[hashed_value] == None:
            self.hashset[hashed_value] = [key]
        else:
            self.hashset[hashed_value].append(key)

    def remove(self, key: int) -> None:
        hashed_value = self.hash_function(key)
        if self.hashset[hashed_value] != None:
            while key in self.hashset[hashed_value]:
                self.hashset[hashed_value].remove(key)

    def contains(self, key: int) -> bool:
        hashed_value = self.hash_function(key)
        if self.hashset[hashed_value] != None:
            return key in self.hashset[hashed_value]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)