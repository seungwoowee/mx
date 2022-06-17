import sys

sys.stdin = open("input.txt", "r")


def find_three(start, path):
    queue = []
    queue.append(start)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    path[queue[0][0]][queue[0][1]] = -1
    while queue:
        y, x = queue.pop()
        for i in range(4):
            dx_next = dx[i] + y
            dy_next = dy[i] + x
            if path[dy_next][dx_next] == 3:
                return 1
            elif path[dy_next][dx_next] == 0:
                queue.append((dy_next, dx_next))
                path[dy_next][dx_next] = -1
    return 0


for k in range(10):
    test_case = int(input())
    path = [list(map(int, input())) for _ in range(16)]
    for x in range(16):
        for y in range(16):
            if path[y][x] == 2:
                start = (y, x)
    print(f'#{test_case} {find_three(start, path)}')
