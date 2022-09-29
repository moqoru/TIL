from collections import deque
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# .은 빈칸, *는 물, D는 도착지, S는 현재 고슴도치 위치 후보
# Z는 이전에 고슴도치가 방문한 곳.
dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

# 경계선 밖으로 나갔는지 검사
def boundary(x, y):
    return True if 0 <= x < r and 0 <= y < c else False

# 물은 큐에 저장해두고 하나씩 꺼내보면서 4방향 델타탐색으로 1칸씩 범람하게 함
# 물이 채워질 수 있는 곳은 .(빈칸), Z(이전 고슴도치 방문), S(현재 고슴도치 위치)
def flood():
    while water_x:
        x, y = water_x.popleft(), water_y.popleft()
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if boundary(nx, ny) and lst[nx][ny] in (".", "S", "Z"):
                lst[nx][ny] = "*"

# 고슴도치는 셋에 저장해 둔 걸 하나씩 꺼내면서, 이전 위치는 다시 되돌아가지 않도록 Z로 덮어씌움
# 이번 차례에 갈 수 있는 곳을 델타 탐색으로 S로 기록함
def run_away():
    while gosum:
        x, y = gosum.pop()
        lst[x][y] = "Z"
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if boundary(nx, ny):
                # 이번 차례에 비버의 집으로 갈 수 있으면 바로 True 리턴하고 종료
                if lst[nx][ny] == "D":
                    return True
                elif lst[nx][ny] == ".":
                    lst[nx][ny] = "S"
    return False

r, c = map(int, input().split())
lst = [list(input()) for _ in range(r)]
water_x, water_y = deque(), deque() # 물의 x, y좌표를 DFS 연산하기 위해 큐에 저장
gosum = set() # 이번 차례의 고슴도치의 좌표를 저장, x, y 좌표를 따로 저장하면 셋 특성상 중복된 숫자가 지워져버림
ans = 0

# 한 턴마다 고슴도치의 이동 후 물의 범람을 진행
# 고슴도치가 갈 수 있는 곳이 없으면(S가 기록된 곳이 1곳도 없거나) KAKTUS
# 고슴도치가 이번 턴에 비버의 집에 갈 수 있으면 턴 횟수인 ans를 출력
while True:
    ans += 1
    for i in range(r):
        for j in range(c):
            if lst[i][j] == "*":
                water_x.append(i)
                water_y.append(j)
            elif lst[i][j] == "S":
                gosum.add((i, j))

    # 고슴도치 먼저 움직이고 물이 범람하게 해야 함!
    if not gosum:
        print("KAKTUS")
        break
    elif run_away():
        print(ans)
        break
    flood()
