l = int(input())
colors = [int(i) for i in input().split()]
cans = [int(i) for i in input().split()]

dp = [0] * l
dp[0] = 1

for i in range(0, l - 1):
    if colors[i] == colors[i + 1] or cans[i] == colors[i + 1]:
        dp[i + 1] += dp[i]
    if (i + 2 < l) and (colors[i] == colors[i + 2] or cans[i] == colors[i + 2]):
        dp[i + 2] += dp[i]

print(dp[-1] % 947)
