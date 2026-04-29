class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen={ "}":"{", ")":"(" , "]":"["}

        for bracket in s:
            if bracket in closeToOpen:
                if stack and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False