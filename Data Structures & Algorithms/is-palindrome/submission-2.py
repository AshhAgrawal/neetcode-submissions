class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Initialize two pointers
        l = 0
        r = len(s) - 1
        
        # Convert string to lowercase
        # WHY: Case-insensitive comparison
        s = s.lower()
        
        # Traverse from both ends toward center
        while l < r:
            
            # Move left pointer until it points to alphanumeric character
            # WHY: Ignore spaces, punctuation, etc.
            while l < r and not s[l].isalnum():
                l += 1
            
            # Move right pointer until it points to alphanumeric character
            while r > l and not s[r].isalnum():
                r -= 1
            
            # Compare characters at both pointers
            # WHY: Palindrome must match from both ends
            if s[l] != s[r]:
                return False
            
            # Move both pointers inward
            l += 1
            r -= 1
        
        # If all characters matched
        return True