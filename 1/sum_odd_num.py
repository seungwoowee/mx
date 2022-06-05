import sys

sys.stdin = open("sum_odd_num.txt", "r")

for test_case in range(1, int(input()) + 1):
    print(f'#{test_case} {sum([int(kk) for kk in input().split() if int(kk) & 1  == 1])}')

