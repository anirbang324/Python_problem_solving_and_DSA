def deecitobinary(n):
    assert int(n)==n,'number should be integer type'
    if n==0:
        return 0
    else:
        return n%2+10*deecitobinary(int(n/2))
number=int(input("enter the number: "))
print(deecitobinary(number))