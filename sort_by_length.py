s = sorted(input().split())
s.sort(key=len)
print(*[sum([ord(sym) for sym in word]) for word in s])
