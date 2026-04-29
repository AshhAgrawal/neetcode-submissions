class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) //2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                total = t+nums[i]
                if (total == target):
                    return True
                nextDp.add(total)
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False