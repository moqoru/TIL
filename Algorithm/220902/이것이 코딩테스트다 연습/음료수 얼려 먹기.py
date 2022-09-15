def ice(x, y):
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if 0 <= nx < n and 0 <= ny < m and not lst[nx][ny]:
            lst[nx][ny] = 1
            ice(nx, ny)

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
n, m = map(int, input().split())
lst = [list(map(int, input())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if not lst[i][j]:
            ice(i, j)
            cnt += 1

print(cnt)