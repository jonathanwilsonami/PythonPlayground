def removeDuplicates(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != None:
            if nums[i] == nums[i+1]:
                if nums[i+1] != None:
                    nums[i+1] = nums[i+2]
                
        else:
            count = count + 1

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums1))
print(removeDuplicates(nums2))
