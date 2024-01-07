arr = list(map(int, input().split()))
st = []

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in st:
            st.append(arr[i])

print(set(st))
