
def gcs(a: list, b: list) -> list[list[int]]:
    n = len(a)
    m = len(b)
    dp = [[0]*(n+1) for _ in range(0, m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])
    return dp


def gcs_answer(a: list, b: list) -> list:
    dp = gcs(a, b)
    i, j = len(a), len(b)
    res = []
    while i > 0 and j > 0:
        if dp[i][j] - dp[i-1][j-1] == 1 and a[i-1] == b[j-1]:
            res.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1
    return res[::-1]

a = list('duck')
b = list('truck')
print(*gcs_answer(a, b), sep='\n')
