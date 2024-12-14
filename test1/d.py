x, y = [int(i) for i in input().split()]
command = input()
while command != 'stop':
    comd_parsed = command.split()[0]
    l = int(command.split()[1])
    if comd_parsed == 'left': x -= l
    elif comd_parsed == 'right': x += l
    elif comd_parsed == 'top': y += l
    elif comd_parsed == 'down': y -= l
    command = input()

print(x,y)
