from sys import exit

letters = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5,
              'f' : 6, 'g' : 7, 'h' : 8}

black_amount = int(input())
black = []
if black_amount != 0:
    for i in range(black_amount):
        pos = input()
        black.append((letters[pos[0]], int(pos[1])))
pos = input()
white = (letters[pos[0]], int(pos[1]))

if white[1] == 8:
    print(1)
    exit()

dp = [[[0, 0] for i in range(0, 9)] for j in range(0, 9)]
for i in black:
    dp[i[1]][i[0]] = [0, 1]
dp[white[1]][white[0]] = [1, 0]

for i in range(white[1] + 1, 9):
    for j in range(1, 9):
        if j + 1 != 9 and dp[i][j][1] == 1 and dp[i - 1][j + 1][0] != 0:
            dp[i][j][0] += dp[i - 1][j + 1][0]
        if dp[i][j][1] == 1 and dp[i - 1][j - 1][0] != 0:
            dp[i][j][0] += dp[i - 1][j - 1][0]
        if dp[i][j][1] == 0 and dp[i - 1][j][0] != 0:
            dp[i][j][0] += dp[i - 1][j][0]

total = 0
for i in range(1, 9):
    total += dp[8][i][0]
print(total)
