class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for op in tokens:
            if op == "+":
                a = stack.pop()
                b = stack.pop()
                val = a + b
                stack.append(val)
            elif op == "-":
                a = stack.pop()
                b = stack.pop()
                val = b - a
                stack.append(val)
            elif op == "*":
                a = stack.pop()
                b = stack.pop()
                val = a * b
                stack.append(val)
            elif op == "/":
                a = stack.pop()
                b = stack.pop()
                val = int(b/a)
                stack.append(val)
            else:
                stack.append(int(op))
            print(stack)
        return stack[-1]