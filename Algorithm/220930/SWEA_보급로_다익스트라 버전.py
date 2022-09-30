import sys
sys.stdin = open("input.txt")
import heapq

# BFS로 먼저 풀었지만, 다익스트라로 재도전!
# 우선순위 큐 없이 풀 경우 소요시간이 너무 오래 걸려, 우선순위 큐를 사용하도록 변경

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

def boundary(x, y):
    return True if 0 <= x < n and 0 <= y < n else False

def dijkstra(s_x, s_y):
    # 방문한 지점 셋에 시작점을 먼저 저장
    U = {(s_x, s_y)}
    # 유선순위 큐로 사용할 리스트, 새로 추가된 좌표의 상하좌우 부분만 확인해서 거리가 줄어든 경우에만 push
    h_q = []
    # 좌표상의 각 지점에서 시작점까지의 거리
    distance = [[999999] * n for _ in range(n)]
    # 원점에서 시작하므로 0,0과 0,1, 1,0 좌표 지점의 거리는 기본으로 기록해 줌
    distance[s_x][s_y] = 0
    distance[s_x + 1][s_y] = lst[s_x + 1][s_y]
    distance[s_x][s_y + 1] = lst[s_x][s_y + 1]

    # 0,1과 1,0의 거리가 갱신되었으므로 우선순위 큐에 저장
    # 우선순위 큐는 데이터를 튜플로 넣을 수 있으며, 튜플의 첫 값이 정렬 기준이 됨(이 경우에는 distance의 값)
    heapq.heappush(h_q, (distance[s_x + 1][s_y], s_x + 1, s_y))
    heapq.heappush(h_q, (distance[s_x][s_y + 1], s_x, s_y + 1))

    # 좌표평면 전부를 탐색할 때까지 반복
    for _ in range(n * n - 1):
        x, y = -1, -1
        # 거리가 작은 값이 먼저 나오는 우선순위 큐에서 방문하지 않은 지점이 나올 때까지 계속 pop
        for i in range(len(h_q)):
            weight, x, y = heapq.heappop(h_q)
            if (x, y) not in U:
                break
        # 새로 방문한 지점으로 셋에 넣음
        U.add((x, y))
        # 방금 셋에 넣은 지점에 대해 4방향 델타탐색으로 최소 거리 갱신
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            # 거리가 더 짧아지는 경우에만 우선순위 큐에 삽입
            if boundary(nx, ny) and distance[nx][ny] > distance[x][y] + lst[nx][ny]:
                distance[nx][ny] = distance[x][y] + lst[nx][ny]
                heapq.heappush(h_q, (distance[nx][ny], nx, ny))
    return distance[-1][-1]

t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]
    print(f'#{cs + 1} {dijkstra(0, 0)}')
