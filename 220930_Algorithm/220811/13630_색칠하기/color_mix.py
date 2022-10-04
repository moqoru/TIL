import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for cases in range(1, t + 1):

    red = [[0] * 10 for _ in range(10)]                         # 빨간색만 칠할 보드
    blue = [[0] * 10 for _ in range(10)]                        # 파란색만 칠할 보드
    n = int(input())                                            # 칠하는 횟수
    lst = [list(map(int, input().split())) for _ in range(n)]   # 칠할 데이터를 2차원 리스트로 한번에 받음
    cnt = 0                                                     # 둘 다 칠해진 칸 갯수

    for k in range(n):                                          # 칠하는 횟수만큼 루프
        for i in range(lst[k][0], lst[k][2] + 1):               # 칠할 칸의 x좌표
            for j in range(lst[k][1], lst[k][3] + 1):           # 칠할 칸의 y좌표
                if lst[k][-1] == 1:                             # 색상 값이 빨간색이라면
                    red[i][j] = 1                               # 빨간색 보드에 칠함
                else:                                           # 색상 값이 파란색이라면... 이하 동일
                    blue[i][j] = 1                              # 참고로 칠한 자리 또 칠하더라도 그냥 1로 기록됨
                if red[i][j] == blue[i][j] == 1:                # 칠한 뒤 바로 두 색상이 다 칠해졌는지 체크 가능
                    cnt += 1                                    # 빨강, 파랑 보드 다 칠했으면 색칠된 칸 수 증가

    print(f'#{cases} {cnt}')