class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        m = len(word1)
        n = len(word2)
        out = ""
        for i in range(m):
            out += word1[i]
            out += word2[i] if i<n else ""
        out += word2[m:] if m<n else ""
        return out