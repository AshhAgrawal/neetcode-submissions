class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        # Convert list of strings into a single string
        for s in strs:
            # Store length of string + delimiter "#" + actual string
            # WHY:
            # - Length helps us know how many characters to read during decoding
            # - "#" acts as separator between length and string
            encoded += str(len(s)) + "#" + s

        return encoded 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # pointer to traverse encoded string

        # Iterate through encoded string
        while i < len(s):
            j = i

            # Find delimiter "#"
            # WHY: Everything before "#" is the length of the string
            while s[j] != "#":
                j += 1

            # Extract length of current string
            length = int(s[i:j])

            # Extract actual string using length
            # WHY: We know exactly how many characters to read
            res.append(s[j+1 : j+1 + length])

            # Move pointer to start of next encoded string
            i = j + 1 + length

        return res