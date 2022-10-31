# 조합의 종류의 수가 많지 않아서 브루트 포스로도 충분할지도?

import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open('input.txt')

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

def boundary(x, y):
    return True if 0 <= x < N and 0 <= y < N else False

def bfs(sx, sy):
    rangeEachLst = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((sx, sy))
    rangeEachLst[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if boundary(nx, ny) and lst[nx][ny] != 1:
                q.append((nx, ny))
                rangeEachLst[nx][ny] = rangeEachLst[x][y] + 1

def virusSelect()

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
virusLst = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            virusLst.append((i, j))

for vx, vy in virusLst:
    bfs(vx, vy)