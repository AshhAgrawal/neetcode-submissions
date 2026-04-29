class Solution:
    def climbStairs(self, n: int) -> int:
        
        # one → ways to reach current step (dp[i])
        # two → ways to reach previous step (dp[i-1])
        # WHY: This is Fibonacci — current = previous + before previous
        one, two = 1, 1

        # We already know base cases for step 0 and 1
        # So we iterate n-1 times to build up to step n
        for i in range(n - 1):

            # Store current value before updating
            # WHY: We need old 'one' to update 'two'
            temp = one

            # Update 'one' to represent ways to reach next step
            # WHY: ways[i] = ways[i-1] + ways[i-2]
            one = one + two

            # Update 'two' to previous 'one'
            # WHY: Shift window forward (like Fibonacci)
            two = temp

        # 'one' now holds number of ways to reach step n
        return one