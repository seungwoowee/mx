import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    nums = [[[arr[i][j]] for j in range(4)] for i in range(4)]

    for _ in range(6):
        new_nums = [[[] for _ in range(4)] for _ in range(4)]
        for x in range(4):
            for y in range(4):
                tmp = set()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tx, ty = x + dx, y + dy
                    if tx < 0 or tx == 4 or ty < 0 or ty == 4:
                        continue
                    tmp.update(nums[tx][ty])
                for val in list(tmp):
                    new_nums[x][y].append(val * 10 + arr[x][y])
        nums = new_nums
    tmp = set()
    for x in range(4):
        for y in range(4):
            tmp.update(nums[x][y])
    print('#{} {}'.format(tc, len(tmp)))
