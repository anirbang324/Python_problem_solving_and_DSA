mylist=[1,2,3,4,5,7,8,9,10]
def findmissing(list,n):
    sum1= 10*(10+1)/2
    sum2= sum(list)
    print(int(sum1-sum2))
findmissing(mylist,10)