from sys import exit
l = int(input())

if l % 2 != 0 or l == 0:
    print(0)
    exit()

dp = [0 for i in range(l + 1)]
dp[0], dp[2] = 1, 3
add = 2 * dp[0]

for i in range(4, l + 2, 2):
    dp[i] = 3 * dp[i - 2] + add
    add += 2 * dp[i - 2]

print(dp[-1])
