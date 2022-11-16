def findprod(nums):
    maxprod=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]*nums[j]>maxprod):
                maxprod= nums[i]*nums[j]
                pairs = str(nums[i])+" "+str(nums[j])
    print("values are:")
    print(pairs)
    print("the maximum product is: ", maxprod)
mylist= list(map(int,input("enter the values separated by space: ").split(" ")))
findprod(mylist)
