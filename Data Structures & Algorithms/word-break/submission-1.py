class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # dp[i] → can substring s[i:] be segmented into words from wordDict
        dp = [False] * (len(s) + 1)

        # Base case: empty string is always valid
        # WHY? → once we reach end, it means all previous splits worked
        dp[len(s)] = True

        # Iterate from end → start
        # WHY? → dp[i] depends on future states (dp[i + len(word)])
        for i in range(len(s) - 1, -1, -1):

            # Try every word in dictionary
            for w in wordDict:

                # Check if word fits starting at index i
                # WHY bounds check? → avoid going out of string
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w):

                    # If the remaining substring is valid → current is valid
                    # WHY dp[i + len(w)]?
                    # → after taking word w, rest must also be breakable
                    dp[i] = dp[i + len(w)]

                # If already found valid split → stop early
                # WHY? → no need to check more words
                if dp[i]:
                    break

        # Final answer: can entire string be segmented?
        return dp[0]