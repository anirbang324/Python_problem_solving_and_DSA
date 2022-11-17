def linearsearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1

myarray = list(map(int,input().split(" ")))
element_to_be_searched = int(input())

print(linearsearch(myarray,element_to_be_searched))

#time complexiety : O(n)
#space complexiety : O(1)