class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i        

nums = [2, 7, 11, 15]
target = 9
result = Solution().twoSum(nums, target)
print(result)


