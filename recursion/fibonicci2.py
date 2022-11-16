def fibo2(num):
    if num<2:
        return num

    return fibo2(num-1)+fibo2(num-2)

n=int(input("Enter the number: "))
print(fibo2(n))