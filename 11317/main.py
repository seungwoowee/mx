import sys

sys.stdin = open("sample_input.txt", "r")

factorial = [1]
for i in range(1, 50 + 1):
    factorial.append(factorial[-1] * i)


def Combination(n, r):
    return factorial[n] // (factorial[r] * factorial[n - r])


memo = dict()


def f(n, p, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif p == 1:
        return n <= k
    try:
        return memo[(n, p, k)]
    except:
        memo[(n, p, k)] = res = sum(Combination(n, i) * f(n - i, p - 1, k) for i in range(k + 1))
        return res


def solve():
    n, p = [int(t) for t in input().split()]

    if p == 1:
        return 0
    else:
        p0_win = sum(Combination(n, i + 1) * f(n - i - 1, p - 1, i) for i in range(n))
        return 1 - (p * p0_win) / p ** n


T = int(input())
for test_case in range(1, T + 1):
    print("#%d %0.012f" % (test_case, solve()))
