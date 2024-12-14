from collections import deque

def mul(x, y):
    det = lambda x1, y1, x2, y2: (x1*y2) - (y1*x2)
    x1, y1, z1 = y
    x2, y2, z2 = x
    return (det(y1, z1, y2, z2),
            det(x1, z1, x2, z2),
            det(x1, y1, x2, y2))

inp = input().split()
stack = deque()
add = lambda x, y: tuple(a+b for a, b in zip(x, y))
for oper in inp:
    if oper == '*':
        stack.append(mul(stack.pop(), stack.pop()))
    elif oper == '+':
        stack.append(add(stack.pop(), stack.pop()))
    else:
        stack.append(tuple(int(i) for i in oper.split(',')))

print(*stack[-1], sep=',')
