def permutation(list1,list2):
    if (len(list1)!=len(list2)):
        return False
    list1.sort()
    list2.sort()
    if(list1==list2):
        return True
    else:
        return False
mylist1=list(map(int,input().split()))
mylist2=list(map(int,input().split()))
print(permutation(mylist1,mylist2))