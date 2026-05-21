class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            n = len(nums)
            memo = [-1] * n

            def dfs(i):
                if memo[i] != -1:
                    return memo[i]

                LIS = 1
                for j in range(i + 1, n):
                    if nums[i] < nums[j]:
                        LIS = max(LIS, 1 + dfs(j))

                memo[i] = LIS
                return LIS

            return max(dfs(i) for i in range(n))

        return lis([e[1] for e in envelopes])