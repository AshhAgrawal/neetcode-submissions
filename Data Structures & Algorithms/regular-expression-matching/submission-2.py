class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # m → length of string s
        # n → length of pattern p
        m = len(s)
        n = len(p)

        # dp cache → stores result for state (i, j)
        # WHY: Avoid recomputing overlapping subproblems
        dp = {}

        def dfs(i, j):
            # Base case: if we reached end of pattern
            # WHY: Match only if we also consumed entire string
            if j == n:
                return i == m

            # Return cached result if already computed
            # WHY: Same (i, j) → same remaining problem
            if (i, j) in dp:
                return dp[(i, j)]

            # Check if current characters match
            # Conditions:
            # 1. i < m → still characters left in s
            # 2. characters match OR pattern has '.'
            # WHY: '.' matches any single character
            match = (i < m) and (s[i] == p[j] or p[j] == ".")

            # Case 1: Next character in pattern is '*'
            # WHY: '*' means zero or more of the previous character
            if j + 1 < n and p[j + 1] == "*":

                # Two options:
                # 1. Skip this pattern (zero occurrences)
                #    → move j by 2 (skip char + '*')
                # 2. Use '*' (if match), consume one char from s
                #    → move i forward, stay at same j to allow repetition
                dp[(i, j)] = (
                    dfs(i, j + 2) or
                    (match and dfs(i + 1, j))
                )
                return dp[(i, j)]

            # Case 2: No '*', but characters match
            # WHY: Move both pointers forward
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            # Case 3: No match
            # WHY: Pattern cannot match string from this state
            dp[(i, j)] = False
            return dp[(i, j)]

        # Start matching from beginning of both string and pattern
        return dfs(0, 0)