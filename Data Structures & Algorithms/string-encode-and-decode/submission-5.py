class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "$" + s
        print("".join(encoded))
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            length = int(s[i:j])
            word = s[j+1: j + 1 + length]
            i = j + 1 + length
            res.append(word)
        return res