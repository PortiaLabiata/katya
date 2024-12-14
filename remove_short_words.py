s = input().split()
ans = 0
for word in s:
    if len(word) >= 5:
        print(sum([ord(sym) for sym in word]), end=' ')
