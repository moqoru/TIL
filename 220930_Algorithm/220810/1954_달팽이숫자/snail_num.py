import sys
sys.stdin = open('input.txt')

t = int(input())                                        # 케이스 횟수 입력받음

for cases in range(1, t + 1):

    n = int(input())                                    # 상자 크기 입력받음
    lst = [[0]*n for _ in range(n)]                     # n * n 크기의 리스트 생성
    di = [(0, 1), (1, 0), (0, -1), (-1, 0)]             # 숫자 진행 방향을 담은 리스트 생성
    x, y, di_now = 0, 0, 0                              # x,y 좌표와 숫자 진행 방향을 기록할 변수

    for i in range(1, n**2 + 1):                        # n^2까지 반복
        lst[x][y] = i                                   # 현재 위치에 현재 숫자 기록

        if di_now == 0:                                 # 진행 방향별로 검사
            if y + 1 >= n or lst[x][y + 1] != 0:        # 밖으로 튀어나가거나 진행방향 다음 칸에 숫자가 있으면
                di_now += 1                             # 진행방향 변경
        elif di_now == 1:                               # 이후 구문들도 방식은 동일함
            if x + 1 >= n or lst[x + 1][y] != 0:
                di_now += 1
        elif di_now == 2:
            if y - 1 < 0 or lst[x][y - 1] != 0:
                di_now += 1
        else:
            if x - 1 < 0 or lst[x - 1][y] != 0:
                di_now = 0                              # 3일 경우에는 다음 방향을 참조하려면 0이 되어야 함

        x, y = x + di[di_now][0], y + di[di_now][1]     # 체크가 끝났다면 x, y 좌표를 진행방향에 맞게 이동
                                                        # 마지막 루프에서는 다른 숫자가 있는 칸으로 가지만 상관 X
    print(f'#{cases}')                                  # 완성된 달팽이 리스트 출력
    for i in range(n):
        for j in range(n):
            print(lst[i][j], end=' ')
        print()