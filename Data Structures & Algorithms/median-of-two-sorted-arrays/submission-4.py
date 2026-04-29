class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Always binary search on the smaller array
        # WHY? → ensures O(log(min(m,n))) complexity and avoids index issues
        if m > n:
            A, B = B, A
            m, n = n, m

        total = m + n
        half = total // 2  # number of elements in left partition

        l, r = 0, m - 1

        while True:
            # Partition index for A
            i = (l + r) // 2

            # Partition index for B
            # WHY -2? → because i and j represent LEFT partition ends
            j = half - i - 2

            # Get boundary elements around partitions
            # Use -inf / +inf to handle edge cases cleanly
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < m else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < n else float("inf")

            # Check if correct partition is found
            # WHY? → all left elements must be ≤ all right elements
            if Aleft <= Bright and Bleft <= Aright:

                # If total length is odd
                # median = smallest element in right partition
                if total % 2:
                    return min(Aright, Bright)

                # If even → average of two middle elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # If A's left element is too big → move partition left
            # WHY? → we included too many elements from A
            if Aleft > Bright:
                r = i - 1
            else:
                # Otherwise move right
                # WHY? → we need more elements from A in left partition
                l = i + 1