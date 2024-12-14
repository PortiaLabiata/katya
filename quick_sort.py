from random import randint

def quick_sort(a: list, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(a) - 1

    if end <= start: return
    i = start
    j = end - 1
    while i < j:
        while a[i] < a[end]:
            i += 1
        while j >= start and a[j] >= a[end]:
            j += 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[i], a[end] = a[end], a[i]
    quick_sort(a, start, i-1)
    quick_sort(a, i+1, end)

if __name__ == '__main__':
    a = list(randint(0, 100) for i in range(0, 10))
    print(*a)
    quick_sort(a)
    print(*a)
