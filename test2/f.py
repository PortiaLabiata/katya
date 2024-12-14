n, k = [int(i) for i in input().split()]
coords = [int(i) for i in input().split()]

def valid(ds, d):


x = -1
diff = []
for i in range(0, len(coords)-1):
    diff.append(coords[i+1] - coords[i])
z = sum(diff)
i = z
while i >= 1:
    while
