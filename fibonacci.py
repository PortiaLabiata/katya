n = int(input())
dp = [1, 1] + [0]*(n-1)

def fib(n):
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]

print(fib(n))
