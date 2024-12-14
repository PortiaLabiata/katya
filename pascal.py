n = int(input())
triangle = [[0 for i in range(0, j+1)] for j in range(0, n+1)]
for i in range(0, n+1):
    triangle[i][0] = triangle[i][-1] = 1

for i in range(2, n+1):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

for i in triangle:
    print(' '.join([str(j) for j in i]))
