import sys
input = sys.stdin.readline

lst = [[False] * 101 for _ in range(101)]
ans_cnt = 0

for t in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if not lst[i][j]:
                ans_cnt += 1
            lst[i][j] = True

print(ans_cnt)