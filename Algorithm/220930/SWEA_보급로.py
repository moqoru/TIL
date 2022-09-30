import sys
sys.stdin = open("input.txt")

from collections import deque
dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

def boundary(x, y):
    return True if 0 <= x < n and 0 <= y < n else False

t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]
    ans_lst = [[9999999] * n for _ in range(n)]
    ans_lst[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if boundary(nx, ny):
                next_weight = ans_lst[x][y] + lst[nx][ny]
                if next_weight < ans_lst[nx][ny]:
                    q.append((nx, ny))
                    ans_lst[nx][ny] = next_weight
    print(f'#{cs + 1} {ans_lst[-1][-1]}')
