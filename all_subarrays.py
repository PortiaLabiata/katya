a = list(map(int, input().split()))

def all_subarrays(a, start, end):
    if start > end:
        return all_subarrays(a, 0, end+1)
    if end == len(a):
        return
    print(*a[start:end+1])
    return all_subarrays(a, start+1, end)

all_subarrays(a, 0, 0)
