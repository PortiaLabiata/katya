y, x = [int(i) for i in input().split()]

ways = [ [0] * 10 for i in range(9) ]
ways[x][y] = 1

for i in range(x + 1, 9):
    for j in range(1, 9):
        ways[i][j] = ways[i - 1][j - 1] + ways[i - 1][j + 1]

print(sum(ways[8]))
