def fibo(n):
    assert n>=0 and int(n)==n,'number is invalid'
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
b=int(input("enter a number: "))
print(fibo(b))