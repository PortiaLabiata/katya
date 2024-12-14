from operator import itemgetter

def merge(a, b, key) -> list:
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if key(a[i]) < key(b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1
    return merged

def merge_sort(l, key=lambda x: x) -> list:
    if len(l) == 1:
        return l
    else:
        right = merge_sort(l[len(l)//2:], key)
        left = merge_sort(l[:len(l)//2], key)
        return merge(left, right, key)

results = []
n = int(input())

for _ in range(0, n):
    k = int(input())
    for _ in range(0, k):
        entry = input().split()
        results.append((float(entry[0]), entry[1]))

results = merge_sort(results, key=itemgetter(1))
results = merge_sort(results, key=itemgetter(0))
print(len(results))
for entry in results[::-1]:
    print(format(entry[0], '.2f'),entry[1])
