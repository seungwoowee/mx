import sys

sys.stdin = open("sample_input.txt", "r")

for tc in range(int(input())):
    n, m, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(n)]
    profit = [0] * n

    for a in range(n):
        for b in range(n - m + 1):
            li = honey[a][b:b + m]

            for c in range(1, 1 << m):
                s = 0
                ss = 0
                for d in range(m):
                    if c & (1 << d) and s + li[d] <= C:
                        s += li[d]
                        ss += li[d] * li[d]
                if ss > profit[a]:
                    profit[a] = ss
    profit.sort()
    print('#{} {}'.format(tc + 1, sum(profit[n - 2:])))
