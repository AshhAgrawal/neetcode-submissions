class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, it's impossible for any permutation to exist in s2
        if len(s1) > len(s2):
            return False

        # Count arrays for characters (fixed size 26 for lowercase letters)
        # WHY array instead of hashmap?
        # → Faster (O(1)) and constant space since only 26 chars
        count1 = [0] * 26
        count2 = [0] * 26

        # Build frequency count for s1 and first window of s2
        for i in range(len(s1)):
            # Map character to index (0–25)
            # WHY ord? → convert char to numeric index for array access
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1
        
        # If first window already matches, we found a permutation
        # WHY equality check works?
        # → Same frequency means same characters → permutation exists
        if count1 == count2:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add new character entering the window
            count2[ord(s2[i]) - ord("a")] += 1

            # Remove character leaving the window
            # WHY i - len(s1)? → start of previous window
            count2[ord(s2[i - len(s1)]) - ord("a")] -= 1

            # Check if current window matches s1
            # WHY check every step?
            # → Sliding window ensures we check all substrings of size len(s1)
            if count1 == count2:
                return True
        
        # If no window matched, no permutation exists
        return False