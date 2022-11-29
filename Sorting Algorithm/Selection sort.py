# in selection sort, we need to repeatedly find the minimum element and move it
# to the sorted part of the array to sort all the elements.

def selectionsort(nums):
    for i in range(len(nums)):  # ....O(n)
        min_index = i
        for j in range(i + 1, len(nums)):  # ....O(n)
            if nums[min_index] > nums[j]:
                min_index = j  # ....O(1)

        nums[i], nums[min_index] = nums[min_index], nums[i]
    print(nums)


mylist = [3, 1, 30, 45, 21]
selectionsort(mylist)

# time complexity : O(n^2)
# space complexity : O(1)
