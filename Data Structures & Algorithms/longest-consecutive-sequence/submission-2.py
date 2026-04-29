class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        unique = set(nums)
        streak = 0

        for i in nums:
            if (i-1) not in unique:
                length = 1
                while (i+length) in unique:
                    length+=1
                streak = max(length,streak)
        return streak