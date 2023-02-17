def catalan(n):
    if (n == 0 or n == 1):
        return 1

    # table to store the results of sub problems
    dp = [0] * (n + 1)

    # initializing the first two values of the table

    dp[0] = 1
    dp[1] = 1

    # filling up the dp[] table using recursive formula

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]


val = int(input("enter the range: "))
for i in range(val):
    print(catalan(i), end=" ")
