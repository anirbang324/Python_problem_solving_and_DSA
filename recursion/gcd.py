def gcd(a,b):
    assert int(a)==a and int(b)==b,'number should be integer'
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if b==0:
        return a
    else:
        return gcd(b,a%b)

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
print(gcd(number1,number2))