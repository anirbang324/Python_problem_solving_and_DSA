def lower1(arr):
    result=[]
    if len(arr)==0:
        return result
    result.append(arr[0].lower())
    return result+lower1(arr[1:])
words=['HI','THERE']
print(lower1(words))