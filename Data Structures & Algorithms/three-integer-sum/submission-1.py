class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Stores all unique triplets
        
        # Sort the array
        # WHY:
        # 1. Enables two-pointer technique
        # 2. Helps in skipping duplicates easily
        nums.sort()
        
        # Iterate through each element as the first number of triplet
        for i, a in enumerate(nums):
            
            # Skip duplicate values for 'a'
            # WHY: Avoid duplicate triplets in result
            if i > 0 and a == nums[i - 1]:
                continue 
            
            # Two pointers for remaining two numbers
            l = i + 1
            r = len(nums) - 1

            # Find pairs such that a + nums[l] + nums[r] == 0
            while l < r:
                sum = a + nums[l] + nums[r]  # Current triplet sum

                # If sum is too large, move right pointer left
                # WHY: Array is sorted → decreasing r reduces sum
                if sum > 0:
                    r -= 1
                
                # If sum is too small, move left pointer right
                # WHY: Increasing l increases sum
                elif sum < 0:
                    l += 1
                
                # Found a valid triplet
                else:
                    res.append([a, nums[l], nums[r]])
                    
                    # Move left pointer forward
                    l += 1
                    
                    # Skip duplicates for second element
                    # WHY: Avoid repeating same pair with same 'a'
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res