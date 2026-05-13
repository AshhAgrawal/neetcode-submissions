class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        # print(n//3)
        for i, c in hashmap.items():
            if c > len(nums)//3:
                res.append(i)
        return res
