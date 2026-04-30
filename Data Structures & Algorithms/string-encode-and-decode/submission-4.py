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
            print(i)
            for j in range(i, len(s)):
                if s[j] == "$":
                    length = int(s[i:j])
                    # i = j-1
                    break
        
            res.append(s[j+1: j+ length + 1])
            i = j+length+1
        return res