import sys
sys.stdin = open('input.txt')

# DFS 탐색, 스택(while 루프) 활용
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

for cs in range(10):
    t = int(input())

    lst = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    stack_x, stack_y = [1], [1]                                         # 스택에 시작 좌표를 기본값으로 넣어둠
    path_found = 0                                                      # 경로를 찾았는지에 대한 정보

    while stack_x:                                                      # 스택이 안 비어 있는 동안 = 갈 길이 있는 동안 탐색
        x, y = stack_x[-1], stack_y[-1]                                 # 스택의 맨 앞 값을 현재 좌표로 가져옴
        stack_add = False                                               # 스택에 새로 값이 추가되었는가에 대한 정보

        for i in range(4):                                              # 4방향으로 탐색
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 16 and 0 <= nx < 16 and visited[nx][ny] != 1:  # 갈 수 있는 길이고 아직 가보지 않은 길이라면

                if lst[nx][ny] == 3:                                    # 도착지를 찾으면 바로 break
                    path_found = 1
                    break

                elif lst[nx][ny] == 0:                                  # 새로 갈 길을 찾으면 stack에 push하고
                    stack_x.append(nx)
                    stack_y.append(ny)
                    visited[nx][ny] = 1                                 # 탐색 완료한 좌표로 기록해줌
                    stack_add = True

        if path_found:                                                  # 도착지를 찾으면 바로 break
            break

        elif not stack_add:                                             # 스택에 값이 추가 안됐다면 = 완전 막다른 곳이라면
            stack_x.pop()                                               # 스택에서 pop
            stack_y.pop()

    print(f'#{t} {path_found}')