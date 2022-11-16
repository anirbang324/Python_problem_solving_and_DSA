def capitalize(arr):
    result=[]
    if len(arr)==0:
        return result
    result.append(arr[0].upper())
    return result+capitalize(arr[1:])

words=['hello','there']
print(capitalize(words))