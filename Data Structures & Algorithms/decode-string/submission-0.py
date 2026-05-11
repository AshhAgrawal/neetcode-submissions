class Solution:
    def decodeString(self, s: str) -> str:
        currString = ""
        currNum = 0
        stack = []

        for char in s:
            if char.isdigit():
                currNum = currNum * 10 + int(char)
            elif char == "[":
                stack.append(currString)
                stack.append(currNum)
                currString = ""
                currNum = 0                
            elif char == "]":
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num * currString
            else:
                currString += char
        return currString