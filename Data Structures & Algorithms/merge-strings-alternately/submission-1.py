class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        m = len(word1)
        n = len(word2)
        out = []
        for i in range(m):
            out.append(word1[i])
            if i<n :
                out.append(word2[i]) 
        if m<n:
            out.append(word2[m:])
        return "".join(out)