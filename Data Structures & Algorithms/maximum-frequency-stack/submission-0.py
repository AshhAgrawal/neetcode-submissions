class FreqStack:

    def __init__(self):
        self.hashmap = {}
        self.stack = {}
        self.maxCount = 0

    def push(self, val: int) -> None:
        valueCount = 1 + self.hashmap.get(val, 0)
        self.hashmap[val] = valueCount
        if valueCount > self.maxCount:
            self.maxCount = valueCount
            self.stack[valueCount] = []
        self.stack[valueCount].append(val)


    def pop(self) -> int:
        res = self.stack[self.maxCount].pop()
        self.hashmap[res] -= 1
        if not self.stack[self.maxCount]:
            self.maxCount -= 1 
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()