# n-Queens 문제 해결 알고리즘 (특정 col만 출력, 해의 총 개수 출력)
def promising(i, col):
    k = 0
    switch = True
    while (k < i and switch == True):  # k가 i보다 작고, 아직 유망하다면 (switch가 True라면)
        if (col[i] == col[k] or abs(col[i] - col[k]) == i - k):  # col[i]를 col[0]부터 col[i-1]까지 비교 - 같은 행 or 같은 대각선 확인
            switch = False  # 그럼 switch를 False로
        k += 1  # k 1 증가
    return switch


def queens(n, i, col):
    global count
    if promising(i, col):  # 만약 i번째 depth column에서 유망하면
        if i == n - 1:  # 끝까지(여기서는 index 6까지) 말을 놨다면
            count += 1  # count 1 증가
            if count == 3:  # 세 번째 해에 도착했다면
                print(col)  # column을 출력한다
        else:  # 아직 말을 놓지 않은 column이 존재하면
            for k in range(n):
                col[i + 1] = k  # 다음 column의 모든 칸에 말을 놓은 후에
                queens(n, i + 1, col)  # 다시 queens를 돌린다


count = 0  # 해 개수 확인용
n = 7
col = n * [0]  # col[i]는 i번째 queen이 위치한 column값
queens(n, -1, col)
print("해의 총 개수 : %d" % count)


road = [list(map(int, input())) for _ in range(n)]


def bfs(G, v):

