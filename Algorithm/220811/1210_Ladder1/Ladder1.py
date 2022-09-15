import sys
sys.stdin = open('input.txt')

for _ in range(10):

    t = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    row, col = 99, -1                                               # 99행에서 시작, 시작 열은 탐색 필요
    direc = [(-1, 0), (0, 1), (0, -1)]                              # 방향 : 위, 오른쪽, 왼쪽
    cur = 0                                                         # 어느쪽 방향인지를 가리킴

    for j in range(100):
        if lst[-1][j] == 2:                                         # 시작점을 찾았다면
            col = j                                                 # 해당 열에서 시작하도록 함
            break

    while row > 0:                                                  # 0행일 때 도착, 아닌 경우 루프 지속
                                                                    # !!이하 if문은 '방향을 바꿀지 말지' 판단하는 구문!!
        if cur == 0:                                                # 위쪽으로 가려는 상황
            if col + direc[1][1] <= 99 and \
                lst[row][col + direc[1][1]] == 1:                   # 칸 밖으로 안 벗어나고 오른쪽으로 갈 수 있으면
                cur = 1                                             # 오른쪽으로 방향 변경

            elif col + direc[2][1] >= 0 and \
                lst[row][col + direc[2][1]] == 1:                   # 마찬가지로 안 벗어나고 왼쪽으로 갈 수 있으면...
                cur = 2                                             # 왼쪽으로 방향 변경

        else:                                                       # 좌 또는 우로 가려는 상황
            if col + direc[cur][1] < 0 or \
                col + direc[cur][1] > 99 or \
                lst[row][col + direc[cur][1]] != 1:                 # 밖으로 벗어나거나 그쪽 방향으로 더이상 갈 수 없으면
                cur = 0                                             # 위쪽으로 방향 변경

        row += direc[cur][0]                                        # 행, 열 좌표를 가려는 방향에 맞게 이동
        col += direc[cur][1]

    print(f'#{t} {col}')                                            # 0행에 도착했다면 그 열의 좌표를 출력