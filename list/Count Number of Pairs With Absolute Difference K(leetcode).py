def countKDifference(nums,k):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (abs(nums[i] - nums[j])) == k:
                count += 1
    return count
mylist = list(map(int,input().split(" ")))
number = int(input())
print(countKDifference(mylist,number))