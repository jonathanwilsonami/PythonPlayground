class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 # Prevent overflow for very large arrays
            if nums[mid] == target:
                return(mid)
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return(-1)
        