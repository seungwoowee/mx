import sys

sys.stdin = open("sample_input.txt", "r")

def count(r, c):
    rr = 0
    cc = 0
    while matrix[r + rr][c + cc]:
        rr += 1
        if r + rr >= n:
            break
    rr -= 1
    while matrix[r + rr][c + cc]:
        cc += 1
        if c + cc >= n:
            break
    cc -= 1
    for i in range(rr + 1):
        for j in range(cc + 1):
            matrix[r + i][c + j] = 0
    return [rr + 1, cc + 1]


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    rec = {}
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                rr, cc = count(i, j)
                rec[rr] = cc
    order_mat = []
    for r in rec.keys():
        if r not in rec.values():
            order_mat.append(r)
            order_mat.append(rec[r])
            break
    while order_mat[-1] in rec:
        order_mat.append(rec[order_mat[-1]])
    dc = len(order_mat)
    dp = [[0] * dc for _ in range(dc)]
    for a in range(1, dc):
        for i in range(1, dc):
            j = i + a
            if j >= dc:
                continue
            min_value = float("inf")
            for k in range(i, j):
                mc = dp[i][k] + dp[k + 1][j] + order_mat[i - 1] * order_mat[k] * order_mat[j]
                min_value = min(min_value, mc)
            dp[i][j] = min_value
    ans = dp[1][-1]
    print(f"#{test_case} {ans}")