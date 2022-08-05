import sys

sys.stdin = open("input.txt", "r")


def LCS(X, Y, N):
    global dp
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    X = input()
    Y = input()
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    LCS(X, Y, N)
    print("#%d %0.02f" % (test_case, dp[N][N] / N * 100))
