import sys
sys.stdin = open('sample_input(1).txt')

cases = int(input())

for t in range(1, cases + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    sum_min, sum_max = 1e7 + 1, 0               # 최소값의 초기값은 10000 x 100개 보다 큰 값이어야 함
    for i in range (n - m + 1):
        sum_now = 0
        for j in range (m):
            sum_now += lst[i + j]               # 이웃한 숫자 합 구함
        if sum_min > sum_now:                   # 최대값, 최소값 갱신
            sum_min = sum_now
        if sum_max < sum_now:
            sum_max = sum_now

    print(f'#{t} {sum_max - sum_min}')