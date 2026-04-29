class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {i: defaultdict(int) for i in range(len(nums) + 1)}
        
        dp[0][0] = 1
        for i in range(len(nums)):
            for sum_, count in dp[i].items():
                dp[i + 1][sum_ + nums[i]] += count
                dp[i + 1][sum_ - nums[i]] += count

        return dp[len(nums)][target]
        