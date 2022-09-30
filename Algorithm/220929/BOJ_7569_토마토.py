# 3차원이고 델타 탐색 방향이 6개라는 것을 제외하면 평범한 BFS 문제

import sys
input = sys.stdin.readline
#sys.stdin = open("input.txt")
from collections import deque

def boundary(a1, a2, a3):
    if 0 <= a1 < M and 0 <= a2 < N and 0 <= a3 < O:
        return True
    else:
        return False

dm = (1, -1, 0, 0, 0, 0)
dn = (0, 0, 1, -1, 0, 0)
do = (0, 0, 0, 0, 1, -1)

M, N, O = map(int, input().split())
putt_tomato = 0 # 덜 익었으니 풋 토마토...?
q_tomato = deque()
lst_3rd = []
for o in range(O):
    tmp_2nd = []
    for n in range(N):
        lst = list(map(int, input().split()))
        for m in range(M):
            if lst[m] == 0:
                putt_tomato += 1
            elif lst[m] == 1:
                q_tomato.append((0, m, n, o))
        tmp_2nd.append(lst)
    lst_3rd.append(tmp_2nd)

if putt_tomato == 0:
    print(0)
else:
    d = 0
    while q_tomato:
        d, m, n, o = q_tomato.popleft()
        for di in range(6):
            nm, nn, no = (
                m + dm[di], n + dn[di], o + do[di]
            )
            if boundary(nm, nn, no) and lst_3rd[no][nn][nm] == 0:
                putt_tomato -= 1
                lst_3rd[no][nn][nm] = 1
                q_tomato.append((d + 1, nm, nn, no))

    print(d) if putt_tomato == 0 else print(-1)