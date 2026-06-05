class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        stack = []

        for b in s:
            if b in ["[", "{","("]:
                stack.append(b)
            elif stack and mapper[b] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False