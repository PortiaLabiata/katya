#This thing would not let me send it
def binary_search(array: list, k: int, l=-1, r=None) -> int:
    if r is None:
        r = len(array)-1
    if r - l <= 1:
        if array[r] == k: return r+1
        else: return -1
    m = (r + l)//2
    if array[m] >= k:
        return binary_search(array, k, l, m)
    else:
        return binary_search(array, k, m, r)

a = list(map(int, input().split()))
k = int(input())

print(binary_search(a, k))
