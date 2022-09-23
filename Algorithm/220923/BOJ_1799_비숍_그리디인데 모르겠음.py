# 풀이 방식이 두 가지가 있는데...
# 1. 체스판에서 이번에 놓은 비숍의 공격 가능한 위치를 전부 지워버리는 방법
# 2. 비숍의 좌표끼리 비교해서 잡을 수 있는지 체크하는 방법
# ...일단 1번을 써 보자.
# set으로 좌표만 저장하게 바꿔도 시간초과 난다...
# 만약, '가장 칠하는 칸 수가 적은 경우' 만 재귀로 들어가게 만든다면...?!

import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

def check_attackable(x, y):
    hap, cha = x + y, x - y
    change = set()
    # for문의 범위를 절반으로 줄일 방법이 없나...?
    for i_f in range(n * 2):
        j_f = hap - i_f # / 방향 대각선
        if 0 <= i_f < n and 0 <= j_f < n and (i_f, j_f) in placeable:
            change.add((i_f, j_f))
        j_f = i_f - cha # \ 방향 대각선
        if 0 <= i_f < n and 0 <= j_f < n and (i_f, j_f) in placeable:
            change.add((i_f, j_f))
    return change

def place_bishop(num_bishop):
    global placeable
    min_num, min_fill = 20, set()
    for i_p, j_p in placeable:
        fill = check_attackable(i_p, j_p)
        if len(fill) < min_num: # 현재 <일 경우 오답, <=일 경우 정답으로 처리되는 상황임.
            min_num = len(fill)
            min_fill = fill.copy()
    placeable = placeable - min_fill
    if len(placeable) == 0:
        global ans
        ans = max(ans, num_bishop + 1)
    else:
        place_bishop(num_bishop + 1)

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
placeable = set()
ans = 0
for i in range(n):
    for j in range(n):
        if lst[i][j]:
            placeable.add((i, j))
if len(placeable) > 0:
    place_bishop(0)
print(ans)