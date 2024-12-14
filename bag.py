def bag(w: list, p: list, size):
    n = len(w)
    dp = [[0]*(size+1) for _ in range(0, n+1)]
    for i in range(1, n+1):
        for j in range(0, size+1):
            if w[i] > j:
                dp[i][j] = d[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], p[i]+dp[i-1][j-w[i]])
