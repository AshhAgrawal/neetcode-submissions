class MyHashSet:

    def __init__(self):
        self.arr = [-1]

    def add(self, key: int) -> None:
        for i in self.arr:
            if key == i:
                return
            else:
                continue
        self.arr.append(key)
        print(self.arr)
        
            

    def remove(self, key: int) -> None:
        for idx, i in enumerate(self.arr):
            if key == i:
                self.arr.pop(idx)
                return
            
    def contains(self, key: int) -> bool:
        for i in self.arr:
            if key == i:
                return True
        return False
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)