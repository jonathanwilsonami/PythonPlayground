
# O(n^2)
def twoSum(nums, target):
    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            b = nums[j]
            if a + b == target:
                return([i, j])

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums1 = [2,7,11,15]

print(twoSum(nums1, 9))