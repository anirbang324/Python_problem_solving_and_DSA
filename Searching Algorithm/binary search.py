import math


def binary_search(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)  # floor is needed to avoid float values
    print(start, middle, end)

    while not (array[middle] == value):
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1

        middle = math.floor((start + end) / 2)
        # print(start,middle,end)
    if array[middle] == value:
        return middle
    else:
        return -1


myarray = list(map(int, input().split(" ")))
element_to_be_searched = int(input())

print("element found at index: ", binary_search(myarray, element_to_be_searched))

# time and space complexity : O(1)
