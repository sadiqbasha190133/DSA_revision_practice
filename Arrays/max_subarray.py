class Solution:
    def maxSubArray(self, nums):
        best = nums[0]
        current = 0
        for num in nums:
            current += num
            if current > best:
                best = current
            if current < 0:
                current = 0
        return best

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))