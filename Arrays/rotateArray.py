class Solution:
    def rotateArray(self, nums, k):
        n = len(nums)
        k = k % n
        if k == 0: return 

        def rev(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        rev(nums, 0, n - 1)
        rev(nums, 0, k - 1)
        rev(nums, k, n - 1)

        return nums
    
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(Solution().rotateArray(nums, k))

        
        

