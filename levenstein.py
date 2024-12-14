def levenshtein(seq1, seq2):
    m = len(seq1) + 1
    n = len(seq2) + 1
    dp = [[[0] for i in range(n)] for j in range(m)]
    for x in range(m):
        dp[x][0] = x
    for y in range(n):
        dp[0][y] = y

    for x in range(1, m):
        for y in range(1, n):
            if seq1[x-1] == seq2[y-1]:
                dp [x][y] = min(dp[x-1][y] + 1,
                    dp[x-1][y-1],
                    dp[x][y-1] + 1)
            else:
                dp [x][y] = min(dp[x-1][y] + 1,
                    dp[x-1][y-1] + 1,
                    dp[x][y-1] + 1)
    return dp[m-1][n-1]

seq1 = input()
seq2 = input()
print(levenshtein(seq1, seq2))
