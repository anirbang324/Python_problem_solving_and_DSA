arr=[1,2,2,3,4,4,5,6,4,5]
a=set(arr)
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            st.append(arr[i])
print(set(st))






