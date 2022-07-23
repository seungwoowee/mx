import sys

sys.stdin = open("input.txt", "r")


dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]


def check_bomb():
    global around_cnt
    for r in range(N):
        for c in range(N):
            if mmap[r][c] == '*':  # 지뢰 : 1
                visited[r][c] = 1
                for d in range(8):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 > nr or nr >= N or 0 > nc or nc >= N:
                        continue
                    if mmap[nr][nc] == '.' and visited[nr][nc] == 0:  # 지뢰 주변 : -1
                        around_cnt += 1
                        visited[nr][nc] = -1
    return bfs()


def bfs():
    global click_cnt, around_cnt
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0:
                continue
            # 주변에 지뢰가 하나도 없는 구역
            q.append((i, j))
            click_cnt += 1  # 클릭 및
            while q:
                r, c = q.pop()
                visited[r][c] = 1  # 주변 칸 숫자 표시 퍼짐
                for d in range(8):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 > nr or nr >= N or 0 > nc or nc >= N:
                        continue
                    if visited[nr][nc] == 0:
                        q.append((nr, nc))
                    elif visited[nr][nc] == -1:  # 지뢰 주변에서는 더 퍼지지 않음
                        visited[nr][nc] = 1
                        around_cnt -= 1  # 지뢰 주변 중에서 숫자 표시 된 칸 제외

    # 클릭 칸 수 = 주변 지뢰 하나도 없는 구역 개수 + 지뢰 주변 중에 숫자 표시 안된 칸 개수
    click_cnt += around_cnt
    return click_cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mmap = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = []
    around_cnt = 0  # 지뢰 인접칸 개수
    click_cnt = 0  # 클릭 칸 개수
    print(f'#{tc} {check_bomb()}')