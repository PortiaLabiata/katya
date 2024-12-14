def levenstein(seq1, seq2, ins, delt, rep):
    m = len(seq1) + 1
    n = len(seq2) + 1
    dp = [[0 for i in range(n)] for j in range(m)]
    for x in range(m):
        dp[x][0] = x*ins
    for y in range(n):
        dp[0][y] = y*ins

    for x in range(1, m):
        for y in range(1, n):
            if seq1[x-1] == seq2[y-1]:
                dp [x][y] = min(dp[x-1][y] + delt,
                    dp[x-1][y-1],
                    dp[x][y-1] + ins)
            else:
                dp [x][y] = min(dp[x-1][y] + delt,
                    dp[x-1][y-1] + rep,
                    dp[x][y-1] + ins)
    return dp[m-1][n-1]

ins, delt, rep = [int(i) for i in input().split()]
a = input()
b = input()
print(levenstein(a, b, ins, delt, rep))
