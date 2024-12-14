from sys import exit
platforms = int(input())

if platforms == 1:
    print(0)
    exit()

heights = []
for i in range(platforms):
    heights.append(int(input()))

dp = [0] * platforms
dp[0], dp[1] = 0, abs(heights[1] - heights[0])

for i in range(2, platforms):
    dp[i] = min(dp[i - 2] + 3 * abs(heights[i] - heights[i - 2]),
                     dp[i - 1] + abs(heights[i] - heights[i - 1]))

print(dp[-1])
