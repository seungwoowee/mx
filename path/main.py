import sys


def bfs(coord, path_length, path, ans):
    while coord:
        new = []

        while coord:
            [x, y] = coord.pop(0)

            for i in range(4):
                x2 = x + dx[i]
                y2 = y + dy[i]
                if 0 <= x2 < path_length and 0 <= y2 < path_length:
                    temp = ans[x][y] + path[x2][y2]
                    if temp < ans[x2][y2]:
                        ans[x2][y2] = temp
                        new.append([x2, y2])

        coord = new

    return ans


sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(int(input())):
    n = int(input())

    road = [list(map(int, input())) for _ in range(n)]
    answer = [[1800 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 0

    answer = bfs([[0, 0]], n, road, answer)

    print(f"#{t + 1} {answer[-1][-1]}")
