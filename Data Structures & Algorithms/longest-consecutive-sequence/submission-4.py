class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        maxl = 0
        for n in nums:
            length = 1
            while (n + length) in sett:
                length += 1
            maxl = max(maxl, length)
            
        return maxl