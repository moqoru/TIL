import sys
sys.stdin = open("input.txt")

from collections import deque

# 동적 계획법으로는 못 푸는 문제, BFS로 진행
# 상좌우하 순서대로 보면서 최소 연료가 갱신되는 경우에만 큐에 새로 넣도록 함
def boundary(x, y):
    return True if 0<=x<n and 0<=y<n else False

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)
t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    min_fuel = [[99999] * n for _ in range(n)]
    min_fuel[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if boundary(nx, ny):
                # x, y에서 nx, ny로 갈 때의 연료를 새로 계산해보고 그 지점의 최소 연료값보다 작다면 갱신 + enqueue
                uphill = max(lst[nx][ny] - lst[x][y], 0)
                if min_fuel[nx][ny] > min_fuel[x][y] + uphill + 1:
                    q.append((nx, ny))
                    min_fuel[nx][ny] = min_fuel[x][y] + uphill + 1

    print(f'#{cs + 1} {min_fuel[-1][-1]}')