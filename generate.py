
def gen_seq(a: list, n: int, prefix=...):
    ''' generate all possible sequences consisting of symbols from a '''
    if prefix is ...:
        prefix = []
    if n == 0:
        print(*prefix)
        return
    for element in a:
        prefix.append(element)
        gen_seq(a, n-1, prefix)
        prefix.pop()

def permutations(a: list, n: int, prefix=...):
    if prefix is ...:
        prefix = []
    if n == 0:
        print(*prefix)
        return
    for i in range(0, len(a)):
        if a[i] is None:
            continue
        prefix.append(a[i])
        a[i] = None
        permutations(a, n-1, prefix)
        a[i] = prefix.pop()


if __name__ == '__main__':
    permutations(list('aboba'), 5)
