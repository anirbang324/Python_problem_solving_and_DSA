# merge sort is divide and conquer algorithm.
# Divide the array into two halves and keep halving until they become too small that can not be broken further.
# merge halves by sorting them.

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]  # left array
        R = arr[mid:]  # right array

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # checking if any element was left

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
    print()


mylist = [4, 1, 361, 6, 7, 1, 1]
mergesort(mylist)
print(mylist)
