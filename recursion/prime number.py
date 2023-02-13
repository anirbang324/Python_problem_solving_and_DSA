def isprime(num, i=2):
    # base condition - if the value is less than 2
    if num <= 2:
        return True if (num == 2) else False
    if num % i == 0:
        return False
    if i * i > num:
        return True

    return isprime(num, i + 1)


n = int(input("enter the number: "))
if isprime(n):
    print("%d is prime" % n)
else:
    print("%d is not prime" % n)
