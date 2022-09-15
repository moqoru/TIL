# 투 포인터 이용한 풀이

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
sticks = [0] * 1001
l_cur, r_cur = 1001, 0
l_max, r_max = 0, 0
polygon_sum = 0

for idx in lst:
    sticks[idx[0]] = idx[1]
    if idx[0] < l_cur:
        l_cur = idx[0]
    if idx[0] > r_cur:
        r_cur = idx[0]

# 조건이 l과 r이 같이 한칸씩 움직이는 게 아님...
# 더 작은 쪽만 움직여야 했던 구조인 거임!!!!
l_max, r_max = sticks[l_cur], sticks[r_cur]

while l_cur < r_cur:




print(polygon_sum)