def permuts(elems, done=[]):
    if len(elems) == 0:
        print(*done)
        return
    for i in range(0, len(elems)):
        permuts(elems[:i]+elems[i+1:], done+[elems[i]])

permuts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
