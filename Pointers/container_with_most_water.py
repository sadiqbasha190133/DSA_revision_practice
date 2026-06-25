class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        best = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            best = max(best, area)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return best

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))