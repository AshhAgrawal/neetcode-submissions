class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        # WHY? → so we can quickly check if a closing bracket matches the last opening one
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []  # stack to track opening brackets

        for b in s:
            # If current char is a closing bracket
            if b in closeToOpen:
                # Check if stack is not empty AND top matches expected opening bracket
                # WHY? → valid pair must match the most recent unclosed bracket (LIFO)
                if stack and stack[-1] == closeToOpen[b]:
                    stack.pop()  # remove matched opening bracket
                else:
                    # Either stack is empty OR mismatch → invalid string
                    return False
            else:
                # If opening bracket, push to stack
                # WHY? → wait for a future closing bracket to match it
                stack.append(b)

        # If stack is empty → all brackets matched correctly
        # If not → some opening brackets were never closed
        return True if not stack else False