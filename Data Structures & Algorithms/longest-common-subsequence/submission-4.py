class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # dp[i][j] → length of LCS between text1[i:] and text2[j:]
        # Extra row & column (len+1) for base cases (empty string)
        dp = [[0 for i in range(len(text2) + 1)] 
                 for j in range(len(text1) + 1)]

        # Traverse from bottom-right → top-left
        # WHY? → dp[i][j] depends on dp[i+1][j], dp[i][j+1], dp[i+1][j+1]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                # If characters match
                if text1[i] == text2[j]:
                    # Take this character + move diagonally
                    # WHY dp[i+1][j+1]? → both strings move forward
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    # Skip one character from either string
                    # WHY?
                    # → try both possibilities and take the best
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # Result is LCS of full strings
        return dp[0][0]