import sys
sys.stdin = open('input.txt')

t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    sum_max = -1
                                                # 4중 포문 안 쓰는 방법을 고민했지만 포기...
    for i in range(n - m + 1):                  # 파리채의 행 방향 시작점
        for j in range(n - m + 1):              # 파리채의 열 방향 시작점
            sum = 0                             # 파리채로 잡았을 때 파리의 마릿수
            for k in range(m):                  # 행 방향으로 파리채 길이만큼 탐색
                for l in range(m):              # 열 방향으로 파리채 길이만큼 탐색
                    sum += lst[i + k][j + l]    # 파리의 마릿수 계산
            if sum > sum_max:                   # 파리의 마릿수 최대치 갱신
                sum_max = sum

    print(f'#{cs + 1} {sum_max}')
