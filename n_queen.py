def printResult(N, Row):
    for i in range(1, N + 1):
        print("(%d, %d)" % (i, Row[i]))
    print("\n")


def promising(q, Row):
    for i in range(1, q):
        if Row[q] == Row[i] or abs(Row[q] - Row[i]) == abs(q - i):
            return False
    return True


def queens(N, q, Row):
    if not promising(q, Row):
        return
    if q == N:
        printResult(N, Row)
        return

    for i in range(1, N + 1):
        Row[q + 1] = i
        queens(N, q + 1, Row)


Row = [0] * 100
N = 4
queens(N, 0, Row)
