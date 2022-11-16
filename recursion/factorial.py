def fact(n):
    assert n>=0 and int(n)==n,'value should be positive integer'
    if n in [0,1]:
        return n
    else:
        return n*fact(n-1)
b=int(input("enter the number:"))
print(fact(b))
