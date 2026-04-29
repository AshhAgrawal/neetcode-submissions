class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, no window needed
        if t == "": return ""

        countT, window = {}, {}

        # Build frequency map of target string t
        # WHY? → We need to know how many of each character are required
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)

        have = 0
        # Number of unique characters we need to match
        need = len(countT)

        l = 0  # left pointer of window
        res = [-1, -1]  # store best window indices
        resLen = float("infinity")  # track smallest window length

        # Expand window using right pointer
        for r in range(len(s)):
            c = s[r]
            # Add current character to window count
            window[c] = 1 + window.get(c, 0)

            # If this character satisfies the required frequency
            # WHY equality? → only when exact match, we consider it "fulfilled"
            if c in countT and window[c] == countT[c]:
                have += 1 
            
            # Try to shrink window when all requirements are satisfied
            # WHY? → We want the minimum length window
            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove left character from window
                window[s[l]] -= 1

                # If removing breaks the requirement, update 'have'
                # WHY? → window is no longer valid after this
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Move left pointer to shrink window
                l += 1

        l, r = res

        # Return smallest valid window substring
        # If no valid window found → return ""
        return s[l:r+1] if resLen != float("infinity") else ""