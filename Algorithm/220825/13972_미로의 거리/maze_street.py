import sys
sys.stdin = open('sample_input(1).txt')

from collections import deque
t = int(input())

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

for cs in range(t):
    n = int(input())
    lst = list(input() for _ in range(n))                               # 주의! 입력 형태가 띄어쓰기가 없음. 문자열 2차원 리스트로 저장됨
    visited = [[0] * n for _ in range(n)]                               # 각 좌표를 방문했는지 여부 기록
    q = deque()                                                         # BFS 방법을 쓰기 위해 큐 사용
    x, y = -1, -1                                                       # 시작점 좌표를 기록할 예정

    for i in range(n):
        if '2' in lst[i]:                                               # 시작점을 찾았으면 x, y에 좌표를 기록해 줌
            x, y = i, lst[i].index('2')
            break

    q.append((x, y, 0))                                                 # 시작점 좌표와 이동 거리를 묶어서 한번에 enqueue
    visited[x][y] = 1                                                   # 시작점도 방문했다고 표시해 줌
    path_len = 0                                                        # 길을 찾은 경우 이동 거리를 저장할 변수

    while q:                                                            # 큐에 값이 있는 동안 = 탐색할 경로가 남아 있는 동안 루프

        x, y, depth = q.popleft()                                       # dequeue해서 x, y좌표와 이동한 거리 받아옴

        for i in range(4):                                              # 4방향 탐색
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1:    # 갈 수 있는 곳이고 안 가본 곳

                if lst[nx][ny] == '3':                                  # 도착점이면 이동 거리 기록해두고 탈출
                    path_len = depth
                    break

                elif lst[nx][ny] == '0':                                # 그냥 통로라면 enqueue해주고 그 좌표의 방문 여부도 기록해 줌
                    q.append((nx, ny, depth + 1))                       # 1칸 더 이동했으므로 이동 거리를 1칸 늘려서 enqueue
                    visited[nx][ny] = 1

        if path_len:
            break

    print(f'#{cs + 1} {path_len}')                                      # 경로를 찾았으면 이동 거리가 출력, 못 찾았으면 기본값 0이 출력
