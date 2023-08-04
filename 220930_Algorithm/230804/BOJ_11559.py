import sys
from collections import deque
input = sys.stdin.readline

# 풀이 순서 : 필드를 탐색하면서 뿌요가 있으면 그 위치에서 BFS 진행
# 체크용 필드를 하나 더 구비해서 그 위치를 탐색했으면 표시해서 무한루프 방지
# 이번 차례에 뿌요가 터졌다면 공중에 떠 있는 뿌요를 내리는 작업 진행
# 안 터졌다면 연쇄가 끝났으므로 바로 출력하고 종료

ROW = 12
COL = 6
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def boundary(x, y):
    return False if x < 0 or y < 0 or x >= ROW or y >= COL else True

field = [list(input().rstrip()) for _ in range(ROW)]

# 뿌요는 최대 18연쇄까지 가능 (6 * 12 / 4 = 18)
for ans in range(20):
    # 탐색했는지 체크, 터졌는지 체크
    chk = [[0] * COL for _ in range(ROW)]
    poped = False

    for i in range(ROW):
        for j in range(COL):

            # 이미 체크한 곳이라면 스킵, 아니라면 체크 먼저 하고 탐색
            if chk[i][j]:
                continue
            chk[i][j] = 1

            # 뿌요를 발견했다면 DFS로 탐색
            if field[i][j] != '.':
                color = field[i][j]
                link = 1
                lx, ly = [i], [j] # 인접한 같은 색깔의 뿌요 좌표 기록
                qx, qy = deque([i]), deque([j])

                while qx:
                    x = qx.popleft()
                    y = qy.popleft()

                    for di in range(4):
                        nx = x + dx[di]
                        ny = y + dy[di]

                        if boundary(nx, ny) and chk[nx][ny] == 0 and field[nx][ny] == color:
                            chk[nx][ny] = 1
                            link += 1
                            lx.append(nx)
                            ly.append(ny)
                            qx.append(nx)
                            qy.append(ny)

                # 4개 이상이라면 터트리는 작업 진행
                if link >= 4:
                    poped = True
                    for p in range(link):
                        px, py = lx[p], ly[p]
                        field[px][py] = "."

    # 안 터졌으면 종료, 터졌다면 공중에 뜬 뿌요 내리기
    if not poped:
        print(ans)
        break
    else:
        for j in range(COL):
            i = ROW - 1
            while i >= 0:
                if field[i][j] != "." and boundary(i + 1, j) and field[i + 1][j] == ".":
                    field[i + 1][j] = field[i][j]
                    field[i][j] = "."
                    i += 1
                else:
                    i -= 1
