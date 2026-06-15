class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        l = 0
        r = len(s) - 1
        s = s.lower()
        while l <= r:
            # print(s[l].isalnum(), s[r].isalnum(), s[l], s[r])
            while not s[l].isalnum() and l < r:
                l+=1
            while not s[r].isalnum() and l < r:
                r-=1    
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
            