class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        # print(hashmap.items())
        arr = []

        for n, i in hashmap.items():
            arr.append([i,n])
            # print(arr)
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        
        return res