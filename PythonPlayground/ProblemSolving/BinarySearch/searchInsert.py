# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
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

nums1 = [1,3,5,6]
nums2 = [1,3]
nums3 = [1,3,5]
nums4 = [3,5,7,9,10]

print(searchInsert(nums4, 8)) #3
print(searchInsert(nums1, 5)) #2
print(searchInsert(nums1, 2)) #1
print(searchInsert(nums2, 2)) #1
print(searchInsert(nums2, 3)) #1
print(searchInsert(nums2, 4)) #2
print(searchInsert(nums1, 7)) #4
print(searchInsert(nums1, 0)) #0
print(searchInsert(nums1, -2)) #0
print(searchInsert(nums2, 0)) #0
print(searchInsert(nums2, 4)) #2

