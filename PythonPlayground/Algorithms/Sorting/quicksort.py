# Without random pivot
def quicksort(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr.pop()
        greater = []
        lower = []

        for i in arr:
            if i > pivot:
                greater.append(i)
            else:
                lower.append(i)

        return quicksort(lower) + [pivot] + quicksort(greater)

test_quick = [5,2,7,1,9,2,5,1,1]

print(quicksort(test_quick))

# With random pivot
import random

def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[left_index], A[i - 1] = A[i - 1], A[left_index]
    return i - 1

def quick_sort_random(A, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        A[pivot], A[left] = (
            A[left],
            A[pivot],
        )  # switches the pivot with the left most bound
        pivot_index = partition(A, left, right)
        quick_sort_random(
            A, left, pivot_index
        )  # recursive quicksort to the left of the pivot point
        quick_sort_random(
            A, pivot_index + 1, right
        )  # recursive quicksort to the right of the pivot point