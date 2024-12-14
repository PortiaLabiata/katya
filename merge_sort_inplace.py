def merge(a, l1, r1, l2, r2):
    i = l1
    j = l2
    while i < r1 or j < r2:
        print(a, i, j, a[i] > a[j])
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            i += 1
        else:
            j += 1


def merge_sort(a, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', a)
    if len(a) == 1:
        return a
    merge_sort(a[:len(a)//2], depth+1, 'left')
    merge_sort(a[len(a)//2:], depth+1, 'right')
    c = merge(left, right)
    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', c)
    return c

a = [1, 3, 5, 2, 4, 6]
merge(a, 0, 2, 3, 5)
print(a)
