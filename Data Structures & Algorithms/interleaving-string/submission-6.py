class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # If lengths don't add up, it's impossible to form s3
        # WHY: Every character in s3 must come from either s1 or s2
        if len(s1) + len(s2) != len(s3):
            return False

        # dp cache → stores results for (i, j)
        # WHY: Avoid recomputing same states → reduces exponential → polynomial
        dp = {}

        def dfs(i, j):
            # Base case: if we've used all chars from s1 and s2
            # WHY: If both are fully consumed, we successfully formed s3
            if i == len(s1) and j == len(s2):
                return True

            # If already computed this state, return stored result
            # WHY: Same (i, j) means same remaining problem
            if (i, j) in dp:
                return dp[(i, j)]

            ans = False  # track if valid interleaving exists from this state

            # Option 1: take character from s1
            # Check:
            # 1. s1 still has characters left
            # 2. current char matches s3 at position (i + j)
            # WHY: i+j represents how many chars we've already used in s3
            if i < len(s1) and s1[i] == s3[i + j]:
                ans = dfs(i + 1, j)

            # Option 2: take character from s2
            # Only try if Option 1 didn't already succeed
            # WHY: Small optimization to avoid unnecessary recursion
            if not ans and j < len(s2) and s2[j] == s3[i + j]:
                ans = dfs(i, j + 1)

            # Store result for current state
            # WHY: Prevent recomputation of same subproblem
            dp[(i, j)] = ans

            return ans

        # Start from beginning of both strings
        return dfs(0, 0)