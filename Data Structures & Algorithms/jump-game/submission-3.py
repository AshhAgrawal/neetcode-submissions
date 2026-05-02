class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i, jump in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + jump)
        return True
    
"""
        i =   [0,1,2,3,4]
Input: nums = [1,2,0,1,0]
               i 
               ^Goal
Output: true
"""



