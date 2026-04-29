class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        print((merged[(length//2) -1]+merged[(length//2)])/2)
        if length%2 != 0:
            return merged[length//2]
        else:
            return (merged[(length//2) -1]+merged[(length//2)])/2
        
        return 0.0