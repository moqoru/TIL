# 풀이 : 길을 북-동-남-서 (시계방향) 순서대로 이어서 긴 선을 만듦
# 긴 선 위에 집을 옮겨서 배치시킴
# 점끼리 직접 이은 경우와, 선 양 끝에 포탈 만들어서 포탈 뚫고 선을 이은 경우 2가지 중 더 짧은 선을 골라 합산

import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
lst = []

for i in range(n + 1):
    dir, p = map(int, input().split())
    if dir == 1:
        lst.append(p)
    elif dir == 4:
        lst.append(w + p)
    elif dir == 2:
        lst.append(2 * w + h - p)
    else:
        lst.append(2 * (w + h) - p)

start = lst[-1]
ans_sum = 0
for idx, val in enumerate(lst[:-1]):
    dir_a = abs(start - val)
    dir_b = 2 * (w + h) - dir_a
    ans_sum += min(dir_a, dir_b)

print(ans_sum)