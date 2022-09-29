# 6방향 델타 탐색인데, 입력값 그대로 쓰려니 왠지 자꾸 틀려서 3차원 리스트로 바꿔서 풀어보니 맞음. 이 뭔...
# 3차원이고 방향이 6개라는 것을 제외하면 평범한 BFS 문제

import sys
#input = sys.stdin.readline
sys.stdin = open("input.txt")
from collections import deque

m, n, h = map(int, input().split())
dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)

lst = [list(map(int, input().split())) for _ in range(n * h)]
putt_tomato = 0 # 안 익었으니 풋토마토...?
q_tomato, q_depth = deque(), deque()
lst_3rd = []

for k in range(h):
    tmp_2nd = []
    for i in range(n):
        tmp_1st = []
        for j in range(m):
            tmp_1st.append(lst[k * n + i][j])
            if lst[k * n + i][j] == 1:
                q_tomato.append((k, i, j))
                q_depth.append(0)
            elif lst[k * n + i][j] == 0:
                putt_tomato += 1
        tmp_2nd.append(tmp_1st)
    lst_3rd.append(tmp_2nd)

if putt_tomato == 0:
    print(0)
else:
    d = 0
    while q_tomato:
        z, x, y = q_tomato.popleft()
        d = q_depth.popleft()
        for di in range(6):
            nz, nx, ny = z + dz[di], x + dx[di], y + dy[di]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and lst_3rd[nz][nx][ny] == 0:
                putt_tomato -= 1
                lst_3rd[nz][nx][ny] = 1
                q_tomato.append((nz, nx, ny))
                q_depth.append(d + 1)
        print(d, lst_3rd)
    print(d) if putt_tomato == 0 else print(-1)