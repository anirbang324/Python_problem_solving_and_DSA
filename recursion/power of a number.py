def pow(base,exp):
    if(exp==0):
        return 1
    if(exp==1):
        return base
    return base*pow(base,exp-1)

b=int(input("Enter base: "))
e=int(input("Enter Exponent: "))
print(pow(b,e))