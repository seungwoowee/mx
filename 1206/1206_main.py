import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    ans = 0
    N = int(input())
    buildings = list(map(int, input().split()))
    for i in range(2, N - 2):
        five_buildings = buildings[i - 2:i + 3]
        if five_buildings[2] == max(five_buildings):
            five_buildings.sort()
            ans += five_buildings[-1] - five_buildings[-2]
    print("#{} {}".format(test_case, ans))
