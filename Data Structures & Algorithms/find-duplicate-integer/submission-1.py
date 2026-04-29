class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat array as a linked list:
        # index → node
        # nums[i] → next pointer
        # WHY? → duplicate creates a cycle in this structure

        slow = fast = 0

        # Phase 1: Detect cycle (find intersection point)
        while True:
            # Move slow by 1 step
            slow = nums[slow]

            # Move fast by 2 steps
            fast = nums[nums[fast]]

            # If they meet → cycle exists
            # WHY? → fast pointer eventually laps slow pointer
            if slow == fast:
                break

        # Phase 2: Find entrance of cycle (duplicate number)
        slow2 = 0  # start from beginning

        while True:
            # Move both pointers one step at a time
            slow = nums[slow]
            slow2 = nums[slow2]

            # They meet at the start of the cycle
            # WHY? → mathematical property of Floyd's algorithm
            if slow == slow2:
                return slow