# 초항이 a, 공차가 d인 길이가 n인 등차수열의 곱을 10^6 + 3 으로 나눈 나머지
# 즉, a x (a + d) x ∙∙∙ x (a + (n - 1)d) 를 10^6 + 3 으로 나눈 나머지
# 채점 서버에서 테스트 케이스의 수가 200만개 정도로 굉장히 많음
#
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 하나의 줄로 이루어지며, 세 개의 정수 a (0 ≤ a ≤ 10^6 + 2), d (0 ≤ d ≤ 10^6 + 2), n (1 ≤ n ≤ 10^9) 가 공백 하나를 사이로 두고 주어짐
#
# [출력]
# 각 테스트 케이스마다, 초항이 a, 공차가 d인 길이가 n인 등차수열의 곱을 10^6 + 3으로 나눈 나머지를 한 줄에 하나씩 출력


import sys

sys.stdin = open("sample_input.txt", "r")
div = int(1e6 + 3)

for test_case in range(1, int(input()) + 1):
    a = [int(kk) for kk in input().split()]
    tmp = 1
    for k in range(0, a[2]):
        if (tmp * (a[0] + k * a[1])) >= 1e6:
            print((tmp * (a[0] + k * a[1])))
        tmp = (tmp * (a[0] + k * a[1])) % div

    print(f'#{test_case} {tmp}')
