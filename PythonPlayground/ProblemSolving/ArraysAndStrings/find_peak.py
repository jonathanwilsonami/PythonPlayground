# Iterative find peak using binary Search O(logn)
def find_peak(nums):
    left = 0
    right = len(nums) - 1
    while(left < right):
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else: 
            right = mid
    print(left)
    print(print(nums[left]))

# Recursive find peak element O(log(n))
def find_peak_rescursive(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return(mid)
        elif arr[mid] < arr[mid + 1]:
            return(find_peak_rescursive(arr,mid+1, right))
        else:
            return(find_peak_rescursive(arr,left, mid))

#######################################################

peak_arr = [1,2,1,4,5,6,7,8,9,10,2]
ans = find_peak_rescursive(peak_arr, 0, len(peak_arr) - 1)
print(ans)


# TODO
# Add Testing