import sys
input = sys.stdin.readline

n = int(input())
lst = [[0] * 101 for _ in range(101)]
cnt = 0

for k in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if lst[i][j] == 0:
                cnt += 1
            lst[i][j] = 1

print(cnt)