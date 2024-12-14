N = 1
HANOI_PATH = []

def hanoi(n, i=1, j=3):
    global HANOI_PATH
    if n == 1:
        HANOI_PATH.append([None, i, j])
        return
    hanoi(n-1, i, 6-i-j)
    HANOI_PATH.append([None, i, 6-i-j])
    hanoi(n-1, 6-i-j, j)

hanoi(2)
print(HANOI_PATH)
