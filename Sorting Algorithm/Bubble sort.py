#bubble sort is also known as sinking sort
#we need to repeatedly compare each pair of adjacent items and swap them if they are in wrong order.

def bubblesort(list):
    for i in range(len(list)-1): #O(n)
        for j in range(len(list)-i-1):  #O(n)
            if list[j] >list[j+1]:  #O(1)
                list[j],list[j+1] = list[j+1],list[j]
    print(list)

mylist = [2,4,1,6,8,5]
bubblesort(mylist)