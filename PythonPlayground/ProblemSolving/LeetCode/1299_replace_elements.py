# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

def replaceElements(arr):
    maxOfRight = -1
    for i in reversed(range(len(arr))):          
        arr[i], maxOfRight = maxOfRight, max(maxOfRight, arr[i])
    return arr
    
test1 = [400]
print(replaceElements(test1))

test2 = [17,18,5,4,6,1]
print(replaceElements(test2)) #[18,6,6,6,1,-1]