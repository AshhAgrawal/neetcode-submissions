class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while j< len(s) and s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1: 1 + length + j]
            # print(word)
            i = 1 + length + j
            out.append(word)
        return out
            


