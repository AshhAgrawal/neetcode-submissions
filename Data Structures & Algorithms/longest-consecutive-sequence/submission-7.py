class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 0
        numSet = set(nums)

        for n in nums:
            if n-1 not in numSet:
                length = n
                currStreak = 0
                while length in numSet:
                    length+=1
                    currStreak+=1
                    streak = max(streak, currStreak)
        return streak
