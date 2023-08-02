import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

# 리스트 밖으로 벗어났는지 판정
def boundary(x, y, n):
    # return True if x < 0 or y < 0 or x >= n or y >= n else False
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    else:
        return True

t = int(input())
for cs in range(1, t + 1):
    n = int(input())
    lst = [[0] * n for _ in range(n)]

    # 우, 하, 좌, 상 순서대로 델타 탐색
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    x, y, di = 0, 0, 0

    # 원소의 갯수만큼 순회
    for cnt in range(1, n * n + 1):
        lst[x][y] = cnt
        nx = x + dx[di]
        ny = y + dy[di]
        # 경계 밖으로 벗어나지 않았고 다른 숫자가 적혀있지 않다면 방향 유지
        if boundary(nx, ny, n) and lst[nx][ny] == 0:
            x, y = nx, ny
        # 아니라면 방향 변경
        else:
            di = (di + 1) % 4
            x += dx[di]
            y += dy[di]

    print(f'#{cs}')
    for i in range(n):
        for j in range(n):
            print(lst[i][j], end=' ')
        print()