from sys import exit

m = int(input())
n = int(input())
p = [[int(input()) for i in range(n)] for j in range(m)]
max_money = int(input())

if m == 1 and n == 1:
    print(max_money)
    exit()
if max_money == 0:
    print(0)
    exit()

dp = [[0]*(n+1) for i in range(0, m+1)]

for j in range(1, n + 1):
    dp[0][j] = 1e6 + 1
for i in range(1, m + 1):
    dp[i][0] = 1e6 + 1
dp[2][1], dp[1][2] = p[1][0], p[0][1]

for i in range(1, m + 1):
    if i == 1:
        for j in range(3, n + 1):
            dp[i][j] = p[i - 1][j - 1] + min( dp[i - 1][j], dp[i][j - 1] )
    elif i == 2:
        for j in range(2, n + 1):
            dp[i][j] = p[i - 1][j - 1] + min( dp[i - 1][j], dp[i][j - 1] )
    else:
        for j in range(1, n + 1):
            dp[i][j] = p[i - 1][j - 1] + min( dp[i - 1][j], dp[i][j - 1] )

min_dp = dp[m][n]
if min_dp <= max_money:
    print(max_money - min_dp)
else:
    print('Impossible')


