class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        mapping = [0] * (n + 1)
        for num in nums:
            mapping[num] += 1

        duplicate = 0
        missing = 0
        for j in range(1, n + 1):
            if mapping[j] == 2:
                duplicate = j
            if mapping[j] == 0:
                missing = j
        return [duplicate, missing]
    
nums = [1,2,2,4]
print(Solution().findErrorNums(nums))
         

