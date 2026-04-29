class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # res[i] will store product of all elements except nums[i]
        # Initialize with 1 (neutral element for multiplication)
        res = [1] * len(nums)

        # prefix → product of all elements to the LEFT of current index
        prefix = 1

        # First pass: fill prefix products
        for i in range(len(nums)):
            
            # Store product of elements before i
            # WHY: prefix already contains product of nums[0...i-1]
            res[i] = prefix

            # Update prefix for next index
            # WHY: include current element for future positions
            prefix *= nums[i]

        # postfix → product of all elements to the RIGHT
        postfix = 1

        # Second pass: multiply postfix products
        for i in range(len(nums) - 1, -1, -1):
            
            # Multiply with product of elements after i
            # WHY: res[i] already has left product → now include right product
            res[i] *= postfix

            # Update postfix for next index
            # WHY: include current element for future positions
            postfix *= nums[i]

        return res