class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hashset = [None] * self.size
    
    def hash_function(self,key):
        return key % self.size

    def add(self, key: int) -> None:
        hashed_function = self.hash_function(key)
        if self.hashset[hashed_function] == None:
            self.hashset[hashed_function] = [key]
        else:
            self.hashset[hashed_function].append(key)

    def remove(self, key: int) -> None:
        hashed_function = self.hash_function(key)
        if self.hashset[hashed_function] != None:
            while key in self.hashset[hashed_function]:
                self.hashset[hashed_function].remove(key) 

    def contains(self, key: int) -> bool:
        hashed_function = self.hash_function(key)
        if self.hashset[hashed_function] != None:
            return key in self.hashset[hashed_function]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)