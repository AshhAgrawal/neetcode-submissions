class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        print(paths)
        for c in paths:
            if c == "..":
                if stack: stack.pop()
            elif c != "" and c != ".":
                stack.append(c)
        print(stack)
        return "/"+"/".join(stack)