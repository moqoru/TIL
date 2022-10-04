t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    min_sum = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not i and not j:
                min_sum[i][j] = lst[i][j]
            elif not i:
                min_sum[i][j] = lst[i][j] + min_sum[i][j - 1]
            elif not j:
                min_sum[i][j] = lst[i][j] + min_sum[i - 1][j]
            else:
                min_sum[i][j] = lst[i][j] + min(min_sum[i - 1][j], min_sum[i][j - 1])

    print(f'#{cs + 1} {min_sum[-1][-1]}')