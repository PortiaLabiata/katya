a = [1, 2, 3, 4]
def shift(a, n):
    for i in range(0, n):
        a.append(a.pop(0))
shift(a, 1)
print(a)
