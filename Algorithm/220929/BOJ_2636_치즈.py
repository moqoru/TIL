from collections import deque
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

# 공기가 통하는 곳은 9, 치즈가 녹은 곳은 2가 되게 했음
# 0, 0 위치를 9로 바꿔준 후, BFS를 진행하면서 상하좌우로 델타탐색해서 0이 있는 자리에 9를 채워넣음
# '다음 단계의 좌표'를 저장할 큐를 만들어 두고, 만약 1을 만나게 되면 그 자리를 2로 채우고(= 닿는 부분을 녹이고) '다음 큐'에 넣음
# 치즈의 갯수를 세서 다 녹았는지 체크, 아직 덜 녹았다면 현재 큐에 '다음 큐'를 복사해서 넣고 그 다음 단계를 반복
# 이번에는 '다음 큐'에 저장되어 있던 좌표들이 곧 공기가 맞닿는 곳이 되기 때문에, 다시 BFS와 델타 탐색을 진행하면 됨.

dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

def boundary(x, y):
    return True if 0<=x<r and 0<=y<c else False

def melt():
    global cheese_cnt
    cnt = 0
    while q_now:
        cnt += 1
        x, y = q_now.popleft()
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if boundary(nx, ny):
                if lst[nx][ny] == 1:
                    q_next.append((nx, ny))
                    cheese_cnt -= 1
                    lst[nx][ny] = 2
                elif lst[nx][ny] == 0:
                    q_now.append((nx, ny))
                    lst[nx][ny] = 9

r, c = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(r)]
cheese_cnt, cheese_prev, ans = 0, 0, 0
q_now, q_next = deque(), deque()

for i in range(r):
    cheese_cnt += sum(lst[i])

cheese_prev = cheese_cnt
lst[0][0] = 9
q_now.append((0, 0))
while q_now:
    ans += 1
    melt()
    if cheese_cnt <= 0:
        print(ans)
        print(cheese_prev)
        break
    q_now = q_next.copy()
    cheese_prev = cheese_cnt
