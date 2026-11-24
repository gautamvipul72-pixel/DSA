def LCS(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
    i = m
    j = n
    lcs = ""
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs = X[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("Length of LCS:", dp[m][n])
    print("Longest Common Subsequence:", lcs)
X = "ABQRMN"
Y = "BQMLRJKN"
LCS(X, Y)