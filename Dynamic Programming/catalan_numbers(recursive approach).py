def cat(n):
    # base case : when n <= 1, return 1
    if n <= 1:
        return 1

    # actual case : iterate from i = 0 to i < n
    # Make a recursive call catalan(i) and catalan(n – i – 1) and keep adding the product of both into res.
    # Return the res.
    res = 0
    for i in range(n):
        res += cat(i) * cat(n - i - 1)
    return res


for i in range(10):
    print(cat(i), end=" ")
