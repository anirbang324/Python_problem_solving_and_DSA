def inunique(list):
    a=[]
    for i in list:
        if i in a:
            print(i)
        else:
            a.append(i)
    return True
mylist= list(map(int,input().split(" ")))
print(inunique(mylist))