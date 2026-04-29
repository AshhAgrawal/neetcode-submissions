class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = {}

        def dfs(i, j):
            if j == n:
                return i == m
            if (i,j) in dp:
                return dp[(i,j)]
            
            match = ((i<m) and ((s[i] == p[j]) or p[j] == "."))
            
            if ( j+1 < n and p[j+1] == "*"):
                dp[(i,j)] = (dfs(i, j+2)                    # we don't take "*" the j+2
                            or (match and dfs(i+1, j)))     # we take "*" then i+1, j so we can calculate how many time char to repeat
                return dp[(i,j)]
            
            if match:
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i,j)]
            dp[(i,j)] = False
            return dp[(i,j)]
        return dfs(0,0)
