class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        minHeap = []
        for key,value in hashmap.items():
            heapq.heappush(minHeap, [value,key])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        # arr.sort()
        res = []
        for i in range(k): 
            res.append(heapq.heappop(minHeap)[1])
        return res