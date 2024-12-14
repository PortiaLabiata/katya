n = int(input())
k = int(input())
a = [int(i) for i in input().split()]
l = -1; r = len(a)-1
while r - l > 1:
    m = (r + l)//2
    if a[m] >= k:
        r = m
    else:
        l = m
if a[r] != k:
    print(-1)
else:
    print(r+1)
