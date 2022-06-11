import sys

sys.stdin = open("input.txt", "r")

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(data, visited, time, S, G):
    q = deque([S])  # (0, 0) 부터 시작
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if (nx, ny) == (0, 0):
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                time[nx][ny] = time[x][y] + data[nx][ny]
                q.append([nx, ny])
            else:
                if time[nx][ny] > time[x][y] + data[nx][ny]:
                    time[nx][ny] = time[x][y] + data[nx][ny]
                    q.append([nx, ny])


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    time = [[0] * n for _ in range(n)]
    S, G = (0, 0), (n - 1, n - 1)

    bfs(data, visited, time, S, G)
    result = time[G[0]][G[1]]

    print('#%d %d' % (tc, result))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(arr):
    queue = arr
    while queue:
        new = []
        while queue:
            [x,y] = queue.pop()
            for i in range(4):
                x2 = x + dx[i]
                y2 = y + dy[i]
                if 0 <= x2 < n and 0 <= y2 < n:
                    temp = ans[x][y] + graph[x2][y2]
                    if temp < ans[x2][y2]:
                        ans[x2][y2] = temp
                        new.append([x2,y2])
        queue = new
for t in range(int(input())):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    ans = [[10000 for _ in range(n)] for _ in range(n)]
    ans[0][0] = graph[0][0]
    bfs([[0,0]])
    print(f"#{t+1} {ans[n-1][n-1]}")