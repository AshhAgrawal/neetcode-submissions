class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Stack to store operands
        # WHY: RPN evaluation uses LIFO (last two operands for each operator)
        stack = []

        # Iterate through each token
        for c in tokens:

            # If operator → perform operation using last two elements
            if c == "+":
                # Pop last two values and push result
                # WHY: order doesn't matter for addition
                stack.append(stack.pop() + stack.pop())

            elif c == "-":
                # Order matters: second popped - first popped
                # WHY: stack.pop() gives last element → so store carefully
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif c == "*":
                # Multiplication (order doesn't matter)
                stack.append(stack.pop() * stack.pop())

            elif c == "/":
                # Division with truncation toward zero
                # WHY: Python // behaves differently for negatives, so use int(b/a)
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                # If number → push to stack
                # WHY: operands are stored until an operator is found
                stack.append(int(c))

        # Final result will be the only element in stack
        return stack[0]