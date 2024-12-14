letters = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
inp = input()
horse = (letters[inp[0]]-1, int(inp[1])-1)
desk = [[0 for i in range(0, 8)] for i in range(0, 8)]

def is_forbidden(pos, h):
    x, y = h
    forbidden = [
        (x-1, y-2),
        (x-1, y+2),
        (x-2, y-1),
        (x-2, y+1),
        (x+1, y-2),
        (x+1, y+2),
        (x+2, y-1),
        (x+2, y+1),
        (x, y)
    ]
    return (pos in forbidden)

for x in range(0, 8):
    if is_forbidden((x, 0), horse):
        break
    desk[x][0] = 1
for y in range(0, 8):
    if is_forbidden((0, y), horse):
        break
    desk[0][y] = 1

for x in range(0, 8):
    for y in range(0, 8):
        if is_forbidden((x, y), horse):
            desk[x][y] = 0
        elif x != 0 and y != 0:
            desk[x][y] = desk[x-1][y] + desk[x][y-1] + desk[x-1][y-1]

'''
for line in desk:
    print(*line, sep='\t')
'''
print(desk[-1][-1])
