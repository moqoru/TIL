import sys
sys.stdin = open('sample_input.txt')

lst = []                                                    # 전체 영역 정보 저장
n = 0                                                       # 영역의 크기
dir_x = (-1, 1, 0, 0)                                       # 움직일 방향 정보 = 델타 탐색
dir_y = (0, 0, -1, 1)

def boundary(x, y, d):                                      # 영역 밖으로 벗어나는지 체크
    if d == 0 and x + dir_x[d] < 0:
        return False
    elif d == 1 and x + dir_x[d] >= n:
        return False
    elif d == 2 and y + dir_y[d] < 0:
        return False
    elif d == 3 and y + dir_y[d] >= n:
        return False
    else:
        return True

def path(x, y):

    result = 0                                              # 리턴할 결과값 저장
    lst[x][y] = 2                                           # 현재 위치를 탐색했다는 의미로 2로 바꿈
    for i in range(4):                                      # 방향별 탐색
        if boundary(x, y, i):                               # 영역 밖을 안 벗어난 경우에만
            x_next, y_next = x + dir_x[i], y + dir_y[i]     # 탐색할 위치 갱신
            if lst[x_next][y_next] == 3:                    # 도착점 발견하면 바로 1 리턴
                return 1
            elif lst[x_next][y_next] == 0:                  # 갈 수 있는 길을 발견했다면
                if path(x_next, y_next):                    # 1을 리턴해 왔을 때만 result 갱신
                    result = 1                              # result = path()로 하면 1로 바꿨더라도 나중에 다른 길에서 허탕 쳐서 도로 0이 되는 불상사가 발생

    return result                                           # 탐색 결과 리턴

t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]       # 숫자가 모두 붙어 있을 경우 input()이라고만 하면 됨, split 안 씀

    start_x, start_y = -1, -1                               # 시작 좌표를 탐색하여 저장
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                start_x, start_y = i, j
                break
        if start_x != -1:
            break

    print(f'#{cs + 1} {path(start_x, start_y)}')            # 시작 좌표를 넣어 함수 호출, 리턴값을 탐색 결과로 출력