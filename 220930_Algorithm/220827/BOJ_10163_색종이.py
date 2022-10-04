import sys
input = sys.stdin.readline

lst = [[0] * 1001 for _ in range(1001)]

n = int(input())
cnt_lst = [0] * (n + 1)

for k in range(1, n + 1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x + w):
        for j in range(y, y + h):
            if lst[i][j] != 0:
                cnt_lst[lst[i][j]] -= 1
            lst[i][j] = k
            cnt_lst[k] += 1

for k in range(1, n + 1):
    print(cnt_lst[k])