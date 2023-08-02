import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

# 주의! 좌우 방향 길이 위쪽 길보다 우선순위가 높으므로, 델타 탐색시 항의 순서를 잘 배치해야 함!
# 좌, 우, 상
dx = (0, 0, -1)
dy = (-1, 1, 0)

def boundary(x, y):
    return False if x < 0 or y < 0 or x >= 100 or y >= 100 else True

for cs in range(1, 11):
    case = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if lst[99][i] == 2:
            x, y = 99, i
            break

    cur = 2 # 기본 방향은 위쪽
    # 맨 윗줄에 도달할 때까지 탐색
    while x > 0:
        # 왼쪽이나 오른쪽 방향으로 가고 있었을 경우
        if cur in (0, 1):
            # 왔던 길을 '되돌아' 갈 수는 없음. 따라서 가던 방향만 체크해야 함
            nx = x + dx[cur]
            ny = y + dy[cur]
            if boundary(nx, ny) and lst[nx][ny]:
                x, y = nx, ny
            # 가던 방향으로 못 가는 경우 무조건 위쪽으로
            else:
                cur = 2
                x += dx[cur]
                y += dy[cur]
        # 위로 가고 있었을 경우
        else:
            # 좌, 우, 상 순서대로 탐색
            for di in range(3):
                nx = x + dx[di]
                ny = y + dy[di]
                if boundary(nx, ny) and lst[nx][ny]:
                    x, y = nx, ny
                    cur = di
                    break

    print(f'#{cs} {y}')