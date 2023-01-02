ints0 = [2,2,2,2,2,1,3,4] # 4, 3, 1
ints = [3,2,2,3] # 3,3
ints2 = [2,2,0,1,2,2,3,0,4,2,2,2] # 0, 1, 3, 0, 4
one_case = [2]
two_case = [2,2]
three_case = [2,2,2]
zero_case = []

ints3 = [1,2,3,0,0,0]
ints4 = [2,5,6]
ints5 = [0,4,4,0,4,4,4,0,2]

def removeElement(nums, val):
    n = len(nums)-1
    while n >= 0:
        if nums[n] == val:
            del nums[n]
        n -=1
    print(nums)

removeElement(two_case, 2)
# removeElement(ints3, 3, ints4, 3)

#Fix later

# def removeElement(self, nums, val):
#     i = 0 
#     j = len(nums)-1
#     if len(nums) == 1:
#         if nums[0] == val:
#             nums.pop()
#     else:
#         while i < j:
#             while nums[j] == val and i <= j:
#                 nums.pop()
#                 j -= 1
#             if i < j and nums[i] == val:
#                 last = nums[j]
#                 nums[j] = nums[i]
#                 nums[i] = last
#                 i += 1
#             else:
#                 i += 1