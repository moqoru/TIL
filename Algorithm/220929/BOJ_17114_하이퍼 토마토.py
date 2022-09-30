import sys
input = sys.stdin.readline
#sys.stdin = open("input.txt")
from collections import deque

def boundary(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
    if 0 <= a1 < M and 0 <= a2 < N and 0 <= a3 < O and 0 <= a4 < P and \
        0 <= a5 < Q and 0 <= a6 < R and 0 <= a7 < S and 0 <= a8 < T and \
        0 <= a9 < U and 0 <= a10 < V and 0 <= a11 < W:
        return True
    else:
        return False

dm = (1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dn = (0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
do = (0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dp = (0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dq = (0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dr = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ds = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0)
dt = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0)
du = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0)
dv = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0)
dw = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1)

M, N, O, P, Q, R, S, T, U, V, W = map(int, input().split())
putt_tomato = 0
q_tomato = deque()
lst_11th = []
for w in range(W):
    tmp_10th = []
    for v in range(V):
        tmp_9th = []
        for u in range(U):
            tmp_8th = []
            for t in range(T):
                tmp_7th = []
                for s in range(S):
                    tmp_6th = []
                    for r in range(R):
                        tmp_5th = []
                        for q in range(Q):
                            tmp_4th = []
                            for p in range(P):
                                tmp_3rd = []
                                for o in range(O):
                                    tmp_2nd = []
                                    for n in range(N):
                                        lst = list(map(int, input().split()))
                                        for m in range(M):
                                            if lst[m] == 0:
                                                putt_tomato += 1
                                            elif lst[m] == 1:
                                                q_tomato.append((0, m, n, o, p, q, r, s, t, u, v, w))
                                        tmp_2nd.append(lst)
                                    tmp_3rd.append(tmp_2nd)
                                tmp_4th.append(tmp_3rd)
                            tmp_5th.append(tmp_4th)
                        tmp_6th.append(tmp_5th)
                    tmp_7th.append(tmp_6th)
                tmp_8th.append(tmp_7th)
            tmp_9th.append(tmp_8th)
        tmp_10th.append(tmp_9th)
    lst_11th.append(tmp_10th)

if putt_tomato == 0:
    print(0) # 다 풀어놓고 이걸 잘못 적어서 24시간을 헤맴. ㅋㅋㅋㅋㅋ
else:
    d = 0
    while q_tomato:
        d, m, n, o, p, q, r, s, t, u, v, w = q_tomato.popleft()
        for di in range(22):
            nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw = (
                m + dm[di], n + dn[di], o + do[di], p + dp[di],
                q + dq[di], r + dr[di], s + ds[di], t + dt[di],
                u + du[di], v + dv[di], w + dw[di]
            )
            if boundary(nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw) and lst_11th[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0:
                putt_tomato -= 1
                lst_11th[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = 1
                q_tomato.append((d + 1, nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw))

    print(d) if putt_tomato == 0 else print(-1)