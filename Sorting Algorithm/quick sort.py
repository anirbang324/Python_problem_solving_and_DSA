# - quick sort is divide and conquer algorithm
# - find pivot number and make sure smaller numbers are located at the left of the pivot and bigger numbers are located
# at the right pivot
# Unlike merge sort, no extra space is required in quick sort.

def partition(arr, low, high):  # function to find partition position
    pivot = arr[high]  # choose the rightmost element as pivot
    i = low - 1  # pointer for greater element

    for j in range(low, high):
        if arr[j] <= pivot:  # if element id smaller than the pivot
            i = i + 1  # swap it with greater element
            (arr[i], arr[j]) = (arr[j], arr[i])

    # swap the pivot element with a greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)


myarray = [6, 7, 1, 2, 3, 4, 1]
quicksort(myarray, 0, len(myarray) - 1)
print(f'sorted array: {myarray}')

# Time complexity : O(nlogn(n))
# Space complexity : O(n)
