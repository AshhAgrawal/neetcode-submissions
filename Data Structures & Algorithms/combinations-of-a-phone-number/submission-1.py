class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6": "mno",
            "7": "pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        i = 0
        res = list(digitsToChar[digits[i]])
        c = 0
        while i < len(digits) - 1:
            if c == 0:
                i+=1
                c = len(res)
            
            while c > 0:
                root = res.pop(0)
                for cc in digitsToChar[digits[i]]:
                    res.append(root+cc)
                c-=1
        return res