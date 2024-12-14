x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

def foldr(a):
    if len(a) == 1:
        return a[0]
    return foldr_or(a[1:])

def is_possible(x1, y1, x2, y2, n):
    if x1 < 0 or y1 < 0 or x1 > 8 or y1 > 8:
        return False
    if x1 == x2 and y1 == y2:
        return n
    if n > 2:
        return -1
    f = []
    f.append(is_possible(x1-1, y1-2, x2, y2, n+1))
    f.append(is_possible(x1-1, y1+2, x2, y2, n+1))
    f.append(is_possible(x1+1, y1-2, x2, y2, n+1))
    f.append(is_possible(x1+1, y1+2, x2, y2, n+1))
    f.append(is_possible(x1-2, y1-1, x2, y2, n+1))
    f.append(is_possible(x1-2, y1+1, x2, y2, n+1))
    f.append(is_possible(x1+2, y1-1, x2, y2, n+1))
    f.append(is_possible(x1+2, y1+1, x2, y2, n+1))
    return foldr_or(f)

if is_possible(x1, y1, x2, y2):
    print(n)
else:
    print(-1)
