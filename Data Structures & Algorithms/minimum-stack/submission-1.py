class MinStack:

    def __init__(self):
        # Main stack stores actual values
        self.stack = []

        # minStack stores the minimum value at each level
        # WHY? → So we can get min in O(1) instead of scanning the stack
        self.minStack = []

    def push(self, val: int) -> None:
        # Push value to main stack
        self.stack.append(val)

        # Compute the new minimum
        # WHY min(val, last min)? → track minimum so far at this position
        # If stack is empty, current value is the min
        val = min(val, self.minStack[-1] if self.minStack else val)

        # Push current minimum to minStack
        # WHY? → keep both stacks in sync
        self.minStack.append(val)

    def pop(self) -> None:
        # Pop from both stacks
        # WHY? → ensure minStack stays aligned with stack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return top of main stack
        # WHY? → standard stack operation
        return self.stack[-1]
        
    def getMin(self) -> int:
        # Return current minimum
        # WHY? → last element in minStack is the minimum so far
        return self.minStack[-1]