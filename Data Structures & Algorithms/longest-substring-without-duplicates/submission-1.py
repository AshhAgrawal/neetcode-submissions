class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # l → left pointer of sliding window
        l = 0

        # Set to store unique characters in current window
        # WHY: Allows O(1) lookup to check duplicates
        charSet = set()

        # res → stores maximum length found
        res = 0

        # r → right pointer expands the window
        for r in range(len(s)):

            # If duplicate found, shrink window from left
            # WHY: Substring must contain unique characters
            while s[r] in charSet:
                charSet.remove(s[l])  # remove leftmost char
                l += 1               # move left pointer forward

            # Add current character to window
            # WHY: Now window has all unique characters
            charSet.add(s[r])

            # Update result with current window size
            # WHY: r - l + 1 gives length of current valid substring
            res = max(res, r - l + 1)

        return res