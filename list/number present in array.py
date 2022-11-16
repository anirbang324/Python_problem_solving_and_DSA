# import numpy as np
# myarray=np.array([1,2,3,4,5,6,7,8,9,10])
def findnum(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            print(i)


myarr = list(map(int, input("enter the array elements separated by space: ").split(" ")))
num = int(input("enter the value you want to find: "))
print("number is present in index: ")
val=findnum(myarr, num)
