arr = []
size1 = int(input("enter the size: "))
element = int(input())
for i in range(0,size1):

    ele = int(input())
    arr.append(ele)
print(arr)
c = 0
# for i in arr:
#     if i==element:
#         c = c+1
#     else:
#         c = 0
# if c > 0:
#     print("element is present")
# else:
#     print("element is not present")


if element in arr: print("element is present");
else: print("element is not present")
