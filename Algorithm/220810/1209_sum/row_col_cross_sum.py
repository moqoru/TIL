import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    row_sum, col_sum, diagonal = [0] * 100, [0] * 100, [0] * 2      # 가로, 세로, 대각선 합을 저장할 리스트
    for i in range(100):
        for j in range(100):
            row_sum[i] += lst[i][j]                                 # 가로줄 합을 i열 위치에 저장
            col_sum[j] += lst[i][j]                                 # 세로줄 합을 j행 위치에 저장
            if i == j:                                              # \ 방향 대각선 위치라면
                diagonal[0] += lst[i][j]                            # \ 대각선 합을 저장
            elif i == abs(99 - j):                                  # / 방향 대각선 위치라면
                diagonal[1] += lst[i][j]                            # 한 줄 길이가 짝수라서 정 중앙은 겹치지 X

    print(f'#{t} {max(max(row_sum), max(col_sum), max(diagonal))}') # 모든 케이스의 max 값을 출력