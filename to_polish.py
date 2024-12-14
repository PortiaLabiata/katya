from collections import deque
opers = deque()
expression = input()
prior = {'+':1, '-':1, '*':2, '/':2, '(':-1}
res = deque()

def is_int(x):
    try:
        aux = int(x)
        return True
    except BaseException:
        return False

for symb in expression:
    print(opers)
    if symb == ' ':
        continue
    if is_int(symb):
        res.append(symb)
    elif symb == '(':
        opers.append(symb)
    elif symb == ')':
        upper = opers.pop()
        while upper != '(':
            res.append(upper)
            upper = opers.pop()
    elif len(opers) == 0:
        opers.append(symb)
    else:
        while len(opers) > 0 and prior[opers[-1]] >= prior[symb]:
            res.append(opers.pop())
        opers.append(symb)

res.extend(opers)
print(*res)
