import sys
input = sys.stdin.readline
#sys.stdin = open('input.txt')
from collections import deque

# 상어의 크기가 성장하는지를 판별하는 함수
def shak_grow(size, stomach):
    global shak_ate
    shak_ate = True
    if stomach + 1 == size:
        return size + 1, 0
    else:
        return size, stomach + 1

def enqueue(x, y, m):
    qx.append(x)
    qy.append(y)
    qmove.append(m)

def dequeue():
    return qx.popleft(), qy.popleft(), qmove.popleft()

def reset_queue():
    qx.clear()
    qy.clear()
    qmove.clear()

# 상, 좌, 우, 하 순서
dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

qx, qy, qmove = deque(), deque(), deque() # 큐에 저장할 탐색가능한 x, y 좌표와 그 턴에서의 이동 거리
shak_x, shak_y, shak_move = -1, -1, 0 # 이번 턴의 상어의 위치와, 상어가 이동한 총합 거리
shak_size, shak_stomach, shak_ate = 2, 0, False # 상어의 크기, 먹은 물고기 마릿수, 밥을 먹었는지 여부
fish = [0] * 7 # 상어보다 작은 물고기가 몇 마리인지 판별하기 위함, 백트래킹 용

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if 1 <= lst[i][j] <= 6:
            fish[lst[i][j]] += 1 # 크기별 물고기 마릿수 기록
        elif lst[i][j] == 9:
            shak_x, shak_y = i, j # 상어 위치 기록

lst[shak_x][shak_y] = 0 # 상어가 있는 위치는 0으로 지워버림.
for i in range(n * n):
    shak_ate = False
    passed = [[0] * n for _ in range(n)] # 상어가 방문했는지 여부를 기록함
    enqueue(shak_x, shak_y, 0) # 큐의 기본 데이터를 넣어 둠
    passed[shak_x][shak_y] = 1 # 상어가 지금 있는 위치도 방문했다고 기록해야 함
    if sum(fish[1: shak_size]) <= 0: # 먹을 수 있는 물고기가 없으면 종료
        break
    min_move = 0 # 같은 이동거리의 물고기끼리 비교하기 위해, 물고기를 먹을 수 있는 최소 이동거리수를 저장해야 함
    eatable = [] # 같은 거리상의 물고기들을 이곳에 담을 예정
    while qx:
        # 같은 우선순위끼리 일단 모아뒀다가 가장 위쪽, 왼쪽에 있는 물고기를 찾아야 함.
        # m의 숫자는 어떻게 맞췄는지 사실 잘 모르겠음...
        x, y, m = dequeue() # 큐에서 데이터를 하나 꺼내서 4방향 탐색
        if min_move and min_move < m + 1: # 물고기를 먹을 수 있는 상황에서 같은 이동거리상에서는 전부 탐색이 끝났다면
            eatable.sort(key=lambda f: (f[0], f[1])) # 가장 왼쪽, 위에 있는 물고기만 골라냄
            shak_x, shak_y = eatable[0][0], eatable[0][1]
            shak_move += m # 총합 이동 거리 갱신
            fish[lst[shak_x][shak_y]] -= 1 # 먹힌 물고기는 1마리 빼 줌
            lst[shak_x][shak_y] = 0 # 원본 리스트에서 먹힌 물고기의 위치는 비움
            shak_size, shak_stomach = shak_grow(shak_size, shak_stomach) # 상어가 성장했나?
            reset_queue()
            break
        for di in range(4): # 4방향 탐색
            nx, ny = x + dx[di], y + dy[di]
            if 0 <= nx < n and 0 <= ny < n:
                # 비어 있거나 같은 크기의 물고기가 있다면 지나갈 수 있음.
                if not passed[nx][ny] and 0 <= lst[nx][ny] <= shak_size:
                    # 물고기를 발견한 경우, 아직 맨 윗줄, 왼쪽이란게 확인이 되지 않으면 바로 먹을 수 없으므로, eatable 리스트에 저장
                    if 1 <= lst[nx][ny] < shak_size:
                        eatable.append([nx, ny])
                        min_move = m + 1 # 물고기를 먹을 수 있는 최소 이동거리 기록
                    enqueue(nx, ny, m + 1) # 다음 탐색 위치를 enqueue
                    passed[nx][ny] = 1 # 지나간 적 있는 곳으로 기록
    if not shak_ate: # 이번 턴에 상어가 굶었어도 종료
        break

print(shak_move)