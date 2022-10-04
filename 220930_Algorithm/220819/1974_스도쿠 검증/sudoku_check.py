import sys
sys.stdin = open('input.txt')

t = int(input())
for cs in range(t):
    lst = [list(map(int, input().split())) for _ in range(9)]   # 스도쿠 판 입력
    ans = 1                                                     # 출력값은 1, 겹치는 숫자가 있으면 0이 될 예정

    for i in range(9):
        sum_r, sum_c, sum_s = 0, 0, 0                           # 가로, 세로, 작은 격자의 합 계산
        x_i, y_i = i // 3 * 3, i % 3 * 3                        # 작은 격자의 좌표를 계산하기 위한 식 1
        # 조합 순서 : 00, 03, 06, 30, 33, 36, 60, 63, 66

        for j in range(9):
            sum_r += lst[i][j]                                  # 가로줄의 합 계산
            sum_c += lst[j][i]                                  # 세로줄의 합 계산
            x_j, y_j = j // 3, j % 3                            # 작은 격자의 좌표를 계산하기 위한 식 2
            # 조합 순서 : 00, 01, 02, 10, 11, 12, 20, 21, 22
            sum_s += lst[x_i + x_j][y_i + y_j]                  # x_i와 x_j, y_i와 y_j를 더해 작은 격자의 좌표를 만들어 총합 구함

        if not sum_r == sum_c == sum_s == 45:                   # 합이 하나라도 45가 아니면 출력값을 0으로 변경
            ans = 0                                             # (1~9까지의 숫자만 있고, 겹치지만 않으면 되므로 총합으로 체크)
            break                                               # 더 이상 루프 돌 필요 없으므로 탈출

    print(f'#{cs + 1} {ans}')