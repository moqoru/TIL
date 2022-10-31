# 입력받은 시험관 리스트를 뒤져서 모든 바이러스의 초기 위치를 파악한 뒤
# 바이러스 번호를 기준으로 정렬하면, 작은 번호의 바이러스가 더 앞에 있게 된다.
# 이 정렬된 리스트를 그대로 큐로 변환하고 BFS를 돌리면,
# 큐 안에서 더 작은 번호의 바이러스가 큰 번호의 바이러스보다 항상 더 앞에 있도록 할 수 있다!
# 이렇게 하면 번호가 낮은 종류의 바이러스부터 먼저 증식한다는 문제의 조건을 깔끔하게 만족시킬 수 있다.

from collections import deque
import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)
q = deque()

def boundary(x, y):
    return True if 0 <= x < N and 0 <= y < N else False

def bfs():
    while q:
        v, x, y = q.popleft()
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if boundary(nx, ny) and not lst[nx][ny]:
                lst[nx][ny] = lst[x][y]
                timePast[nx][ny] = timePast[x][y] + 1
                if timePast[nx][ny] < S:
                    q.append([v, nx, ny])
    return lst[X - 1][Y - 1]

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
timePast = [[-1] * N for _ in range(N)]
virusLocation = []
S, X, Y = map(int, input().split())

for i in range(N):
    for j in range(N):
        if lst[i][j]:
            virusLocation.append([lst[i][j], i, j])
            timePast[i][j] = 0

virusLocation.sort(key=lambda x: x[0])
q = deque(virusLocation)

if S == 0:
    print(lst[X - 1][Y - 1])
else:
    print(bfs())