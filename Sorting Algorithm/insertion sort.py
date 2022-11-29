# We need to divide the given array into two parts - sorted part and unsorted part
# Take the first element from the unsorted array and find it's correct position in the sorted array.
# Repeat the same steps, compare the elements and put them in the sorted array until the unsorted array is empty.


def insertionsort(mylist):
    for i in range(1, len(mylist)):  # ..............O(n)
        key = mylist[i]  # ..............O(1)
        j = i - 1

        while j >= 0 and key < mylist[j]:  # .............O(n)
            mylist[j + 1] = mylist[j]  # .............O(1)
            j -= 1

        mylist[j + 1] = key
    print(mylist)


nums = [2, 5, 1, 7, 1, 4, 5]

insertionsort(nums)

# time complexity : O(n^2)
# space complexity : O(1)
