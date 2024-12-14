l = int(input())
chain = [int(i) for i in input().split()]

dp = [0] * l
dp[0] = 1

for i in range(l - 1):
    if chain[i] + i < l:
        dp[chain[i] + i] += dp[i]
    if chain[i] != 1:
        dp[i + 1] += dp[i]

print(dp[-1] % 937)
