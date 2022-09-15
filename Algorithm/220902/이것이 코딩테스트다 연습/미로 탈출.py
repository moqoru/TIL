from collections import deque
n, m = map(int, input().split())
lst = [list(map(int, input())) for _ in range(n)]
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
q_x = deque([0])
q_y = deque([0])
lst[0][0] = 2
while q_x:
    x, y = q_x.popleft(), q_y.popleft()
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 1:
            q_x.append(nx)
            q_y.append(ny)
            lst[nx][ny] = lst[x][y] + 1
            if nx == n - 1 and ny == m - 1:
                x, y = nx, ny
                break
    if x == n - 1 and y == m - 1:
        break

print(lst[n-1][m-1] - 1)