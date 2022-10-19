import sys

sys.stdin = open("input.txt", "r")


def find_ans(arr_, visited, n, dx, dy):
    max_field, max_height = 1, 0

    while sum([sum(visited[kk]) for kk in range(n)]) != pow(n, 2):
        for k in range(n):
            if sum(visited[k]) != n:
                begin_pos = [[k, visited[k].index(0)]]
                break
        cur_field, cur_height = 1, 0
        while begin_pos:
            new = []
            while begin_pos:
                [y, x] = begin_pos.pop()
                visited[y][x] = 1

                for k in range(4):
                    xx, yy = x + dx[k], y + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        if not visited[yy][xx]:
                            if arr_[y][x] == arr_[yy][xx]:
                                cur_field += 1
                                cur_height = arr_[y][x]
                                new.append([yy, xx])
                                visited[yy][xx] = 1

            begin_pos = new
        if max_field < cur_field:
            max_field = cur_field
            max_height = cur_height

    return max_field, max_height


def after_rain(arr_, visited, n, dx, dy):
    while sum([sum(visited[kk][1:-2]) for kk in range(n)]) != pow(n, 2):
        for k in range(n):
            if sum(visited[k]) != n:
                begin_pos = [[k, visited[k].index(0)]]
                break
        cur_field, cur_height = 1, 0
        while begin_pos:
            new = []
            while begin_pos:
                [y, x] = begin_pos.pop()
                visited[y][x] = 1

                for k in range(4):
                    xx, yy = x + dx[k], y + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        if not visited[yy][xx]:
                            if arr_[y][x] == arr_[yy][xx]:
                                cur_field += 1
                                cur_height = arr_[y][x]
                                new.append([yy, xx])
                                visited[yy][xx] = 1

            begin_pos = new
    return arr_


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for test_case in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    max_field, max_height = find_ans(arr, visited, n, dx, dy)
    arr_ = after_rain(arr, visited, n, dx, dy)

    print("#%d %d %d" % (test_case, max_field, max_height))
