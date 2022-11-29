# pseudo code

# create buckets and distribute elements of array into buckets.
# sort buckets individually
# merge buckets after soring
# formula to find 'number of buckets' - round(sqrt(number of elements))
# formula to find the 'appropriate bucket' where the element will be added - ceil(value*number of buckets/maxvalue)

# source code

import math


def bucketsort(customlist):
    numberofbuckets = round(math.sqrt(len(customlist)))
    maxvalue = max(customlist)
    arr = []  # temporary array to create the buckets

    for i in range(len(customlist)):
        arr.append([])  # depending upon the loop we can add sub arrays.

    for j in customlist:  # to add elements in the sub arrays.
        index_b = math.ceil(j * numberofbuckets / maxvalue)
        arr[index_b - 1].append(j)  # inserting element in the appropriate bucket.

    for i in range(numberofbuckets):
        arr[i] = sorted(arr[i])

    k = 0

    for i in range(numberofbuckets):
        for j in range(len(arr[i])):
            customlist[k] = arr[i][j]
            k += 1

    return customlist


mylist = [7, 4, 1, 8, 4, 2, 9, 1]

print(bucketsort(mylist))

# time complexity : O(n^2)
# space complexity : O(n)
