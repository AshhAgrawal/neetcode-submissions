class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = leftMax = 0

        for i in range(len(s)):
            if s[i] == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif s[i] == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
                # print("here")
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            # print(leftMin, leftMax)
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0