k = int(input())
m = int(input())

def pullups(k, m):
    if m == 1:
        return k+m-1
    return pullups(k, m-1) + (k+m-1)+(k+m-2)

print(pullups(k,m))
