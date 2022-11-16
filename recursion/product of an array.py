def productarr(arr):
    if len(arr)==0:
        return 1
    return arr[0]*productarr(arr[1:])
print(productarr([1,2,3]))