a = [int(i) for i in input().split()]

def selection_sort(a, i=0):
    if len(a) == 1 or (len(a) == 2 and a[0] <= a[1]):
        return
    if i < len(a):
        amin = min(list(range(i, len(a))), key=a.__getitem__)
        a[i], a[amin] = a[amin], a[i]
        if a[i] != a[amin]:
            print(*a)
        selection_sort(a, i+1)

selection_sort(a)
