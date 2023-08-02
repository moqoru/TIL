import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

# 가로줄, 세로줄, 대각선줄 각각의 합 중 가장 큰 합 숫자를 찾기
for cs in range(1, 11):
    case = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    ans = -1
    cross1, cross2 = 0, 0 # 대각선 총합
    for i in range(100):
        cross1 += lst[i][i] # \ 대각선 총합 계산
        cross2 += lst[i][-i - 1] # / 대각선 총합 계산
        curRow, curCol = 0, 0
        for j in range(100):
            curRow += lst[i][j] # 가로줄 총합 계산
            curCol += lst[j][i] # 세로줄 총합 계산
        # 최대값 갱신
        # ans = max(curRow, curCol, ans)
        ans = curRow if curRow > ans else ans
        ans = curCol if curCol > ans else ans
    # ans = max(cross1, cross2, ans)
    ans = cross1 if cross1 > ans else ans
    ans = cross2 if cross2 > ans else ans
    print(f'#{case} {ans}')