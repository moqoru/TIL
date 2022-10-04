import sys
sys.stdin = open('input.txt')

# BFS 탐색, 큐로 풀기
from collections import deque

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

for cs in range(10):
    t = int(input())

    lst = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    qx, qy = deque([1]), deque([1])                                     # 시작점이 1, 1이므로 큐에 초기값으로 저장
    visited[1][1] = 1                                                   # 방문한 지점인지에 대한 정보도 기록
    path_found = 0                                                      # 길을 찾았는가?

    while qx:                                                           # 큐에 데이터가 들어 있으면 = 갈 길이 남아 있으면 루프
        x = qx.popleft()                                                # x, y 좌표 새로 dequeue
        y = qy.popleft()

        for i in range(4):                                              # 4방향 탐색
            nx, ny = x + dx[i], y + dy[i]                               # 탐색할 좌표

            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] != 1:  # 밖으로 안 벗어나고 아직 방문한 적 없으면
                if lst[nx][ny] == 3:                                    # 도착점이라면 찾았다고 기록하고 바로 break
                    path_found = 1
                    break

                elif lst[nx][ny] == 0:                                  # 아직 갈 길이 남아 있다면
                    visited[nx][ny] = 1                                 # 방문한 위치를 기록해 주고
                    qx.append(nx)                                       # x, y 좌표 enqueue
                    qy.append(ny)

        if path_found:                                                  # 도착했다면 더 루프를 돌 필요 없음
            break

    print(f'#{t} {path_found}')