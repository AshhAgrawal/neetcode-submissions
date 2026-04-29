class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Always binary search on the smaller array
        if m > n:
            A, B = B, A
            m, n = n, m

        total = m + n
        half = total // 2

        l, r = 0, m - 1

        while True:
            i = (l + r) // 2      # partition index for A
            j = half - i - 2      # partition index for B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < m else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < n else float("inf")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # A partition is too far right, move left
            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1