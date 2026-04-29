class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0

        # Deque will store indices, not values
        # WHY indices? → so we can check if they are out of window range
        q = collections.deque()

        while r < len(nums):

            # Maintain decreasing order in deque
            # WHY? → front of deque should always be the maximum
            # Remove all smaller elements from the back
            # because they can never be the max if current is bigger
            # print(q, nums[q[-1]] if q else -999)
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add current index
            q.append(r)
            
            # Remove left-most index if it's out of window
            # WHY? → ensure deque only contains elements inside window
            if l > q[0]:
                q.popleft()

            # Once we reach window size k
            if r + 1 >= k:
                # Front of deque is the max of current window
                output.append(nums[q[0]])

                # Move left pointer to shrink window
                l += 1

            # Expand window
            r += 1

        return output