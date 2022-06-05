import sys

sys.stdin = open("input.txt", "r")


def get(seg, s, e, x):
    i, ret = 1, 0
    while s != e:
        seg[i] += 1
        m, ch = (s + e) >> 1, i << 1
        if m < x:
            ret += seg[ch]
            s = m + 1
            i = ch + 1
        else:
            e = m
            i = ch
    seg[i] += 1
    return ret


for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    l = max(arr)
    seg_left = [0] * (1 << (l.bit_length() + 1))
    seg_right = seg_left[:]
    m = 10 ** 9 + 7
    L, R = 0, 0

    for i in range(N):
        L += get(seg_left, 1, l, arr[i])
        R += get(seg_right, 1, l, arr[N - i - 1])

    ans = K * (L * (K - 1) + R * (K + 1)) // 2 % m
    print(f'#{T} {ans}')
