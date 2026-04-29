class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # leftMin → minimum possible open brackets at this point
        # leftMax → maximum possible open brackets at this point
        # WHY: '*' can act as '(', ')' or empty → creates a range of possibilities
        leftMin = leftMax = 0

        for i in range(len(s)):
            
            if s[i] == "(":
                # '(' increases both min and max open brackets
                # WHY: definitely adds an unmatched '('
                leftMin, leftMax = leftMin + 1, leftMax + 1
            
            elif s[i] == ")":
                # ')' decreases both min and max open brackets
                # WHY: it tries to close an existing '('
                leftMin, leftMax = leftMin - 1, leftMax - 1
            
            else:
                # '*' can be:
                # '(' → increases open count
                # ')' → decreases open count
                # ''  → no change
                # So:
                # min decreases (if treated as ')')
                # max increases (if treated as '(')
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            # If max < 0 → even best case cannot balance
            # WHY: too many ')' encountered
            if leftMax < 0:
                return False
            
            # leftMin cannot go below 0
            # WHY: we cannot have negative unmatched '('
            # Clamp it to 0 (treat extra ')' as matched)
            if leftMin < 0:
                leftMin = 0
        
        # At end, check if we can fully balance
        # WHY: valid only if minimum possible open count is 0
        return leftMin == 0