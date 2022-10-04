import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q_x = deque([x])
    q_y = deque([y])
    l_x, l_y = [x], [y]
    visit[x][y] = 1
    cnt, p_sum, p_move = 1, lst[x][y], False

    while q_x:
        px, py = q_x.popleft(), q_y.popleft()
        for di in range(4):
            nx, ny = px + dx[di], py + dy[di]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0 and L<=abs(lst[px][py]-lst[nx][ny])<=R:
                if not p_move and p_sum // cnt != lst[nx][ny]:
                    p_move = True
                visit[nx][ny] = 1
                l_x.append(nx)
                l_y.append(ny)
                q_x.append(nx)
                q_y.append(ny)
                cnt += 1
                p_sum += lst[nx][ny]

    if not p_move:
        return False
    else:
        p_new = p_sum // cnt
        for ch in range(len(l_x)):
            lst[l_x[ch]][l_y[ch]] = p_new
        return True

ans = 0
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

while True:
    visit = [[0] * N for _ in range(N)]
    changed = False
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and bfs(i, j):
                changed = True
    if not changed:
        break
    else:
        ans += 1

print(ans)