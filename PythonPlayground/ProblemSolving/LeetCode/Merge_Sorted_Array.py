ints = [-1,0,0,3,3,3,0,0,0]
ints2 = [1,2,2]

ints3 = [1,2,3,0,0,0]
ints4 = [2,5,6]

def merge(nums1, m, nums2, n):
    nums1_len = len(nums1) - 1
    nums2_len = len(nums2) - 1
    while m <= nums1_len:
        del nums1[nums1_len]
        nums1_len -= 1
    while n <= nums2_len:
        del nums2[nums2_len]
        nums2_len -= 1
    nums1.extend(nums2)
    nums1.sort()


# merge(ints, 6, ints2, 3)
merge(ints3, 3, ints4, 3)

def merge2(self, nums1, m, nums2, n):
    # Initialize nums1's index
    i = m - 1
    # Initialize nums2's index
    j = n - 1
    # Initialize a variable k to store the last index of the 1st array...
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

#https://www.youtube.com/watch?v=P1Ic85RarKY