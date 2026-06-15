class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
      
        arr = []
        for key,v in hashmap.items():
            arr.append([v,key])
        arr.sort()
        res = []
        while k > 0:
            k= k - 1
            res.append(arr.pop()[1])
            
        return res