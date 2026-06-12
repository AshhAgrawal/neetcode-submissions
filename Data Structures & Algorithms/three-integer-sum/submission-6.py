class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue
            j = i+1
            k = n-1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == 0:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                if currSum > 0:
                    k-=1
                else:
                    j+=1
            print(i)
        return res
                
