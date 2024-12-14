
def gis(a: list) -> list:
    n = len(a)
    dp = [0]*n
    for i in range(0, n):
        m = 0
        for j in range(0, i):
            if a[j] < a[i] and dp[j] > m:
                m = dp[j]
        dp[i] = 1 + m
    return dp

def gis_answer(a: list) -> list:
    dp = gis(a)
    n = max(dp)

