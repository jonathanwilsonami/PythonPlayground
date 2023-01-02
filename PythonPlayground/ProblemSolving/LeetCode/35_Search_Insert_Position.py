class Solution(object):
    def searchInsert(self, nums, target):
        left = 0 
        right = len(nums) - 1
        if target <= nums[0]:
            return(0)
        if target > nums[right]:
            return(len(nums))
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return(mid)
            elif target < nums[mid]: 
                if target > nums[mid-1]:
                    return(mid)
                right = mid - 1
            else: 
                left = mid + 1