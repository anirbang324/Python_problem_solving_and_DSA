def sod(n):
    assert n>=0 and int(n)==n,'invalid number'
    if n==0:
        return 0
    else:
        return int(n%10)+sod(int(n/10))
b=int(input("Enter the number" ))
print(sod(b))