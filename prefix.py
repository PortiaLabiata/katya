

def prefix(s: str) -> list[int]:
    n = len(s)
    res = [0]*n
    for i in range(1, n):
        p = res[i-1]
        while p > 0 and s[i] != s[p]:
            p = res[p-1]
        res[i] = (p + 1) if s[i] == s[p] else 0
    return res

def KMP(sub: str, s: str) -> list[int]:
    res = []
    n = len(sub)
    g = sub + '\0' + s
    r = prefix(g)
    for j in range(2*n, len(g)):
        if r[j] == n:
            res.append(j - 2*n)
    return res

if __name__ == '__main__':
    s = 'abcabadabacabafabac'
    print(*s)
    print(KMP('ab', s))
