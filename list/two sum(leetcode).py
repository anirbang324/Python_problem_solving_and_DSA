#find all pairs of integers where sum is equal to the given number
def twosum(nums,t):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]==nums[j]):
                continue
            elif(nums[i]+nums[j]==t):
                print(nums[i],nums[j])
                print(i, j)
mylist= list(map(int,input().split(" ")))
target=int(input("enter the target value: "))
twosum(mylist,target)