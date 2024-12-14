
def hanoy(n: int, i=1, j=3):
    if n == 1:
        print(f'Move from {i} to {j}')
        return
    hanoy(n-1, i, 6-i-j)
    print(f'Move from {i} to {6-i-j}')
    hanoy(n-1, 6-i-j, j)

hanoy(2)

