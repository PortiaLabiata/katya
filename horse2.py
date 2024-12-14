x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

a = [[-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1]]
def solve(x1, y1, n=0):
    global a
    if x1 >= 8 or y1 >= 8 or x1 < 0 or y1 < 0 or n > 2:
        return
    if a[x1][y1] != -1:
        a[x1][y1] = min(n, a[x1][y1])
    else:
        a[x1][y1] = n
    solve(x1-1, y1-2, n+1)
    solve(x1-1, y1+2, n+1)
    solve(x1+1, y1-2, n+1)
    solve(x1+1, y1+2, n+1)
    solve(x1-2, y1-1, n+1)
    solve(x1-2, y1+1, n+1)
    solve(x1+2, y1-1, n+1)
    solve(x1+2, y1+1, n+1)

solve(x1-1, y1-1)
print(a[x2-1][y2-1])
