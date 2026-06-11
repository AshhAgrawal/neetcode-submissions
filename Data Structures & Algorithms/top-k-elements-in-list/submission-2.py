class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        arr = []
        for key,value in hashmap.items():
            arr.append([value, key])
        arr.sort()
        res = []
        for i in range(k): 
            res.append(arr.pop()[1])
        return res