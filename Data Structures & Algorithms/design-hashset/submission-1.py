class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.arr = [[] for _ in range(self.size)]    

    def add(self, key: int) -> None:
        correctBucket = key % self.size
        bucket = self.arr[correctBucket]

        if key not in bucket:
            bucket.append(key)


    def remove(self, key: int) -> None:
        correctBucket = key % self.size
        bucket = self.arr[correctBucket]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        correctBucket = key % self.size
        bucket = self.arr[correctBucket]

        return key in bucket

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)