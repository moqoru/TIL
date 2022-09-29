import sys
#input = sys.stdin.readline
sys.stdin = open("input.txt")
from collections import deque

def boundary(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
    if 0 <= a1 < N and 0 <= a2 < O and 0 <= a3 < P and 0 <= a4 < Q and \
        0 <= a5 < R and 0 <= a6 < S and 0 <= a7 < T and 0 <= a8 < U and \
        0 <= a9 < V and 0 <= a10 < W and 0 <= a11 < M:
        return True
    else:
        return False

dn = (1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
do = (0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dp = (0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dq = (0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dr = (0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
ds = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
dt = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0)
du = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0)
dv = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0)
dw = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0)
dm = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1)

M, N, O, P, Q, R, S, T, U, V, W = map(int, input().split())
putt_tomato = 0
q_tomato, q_depth = deque(), deque()
lst_11th = []
for n in range(N):
    tmp_10th = []
    for o in range(O):
        tmp_9th = []
        for p in range(P):
            tmp_8th = []
            for q in range(Q):
                tmp_7th = []
                for r in range(R):
                    tmp_6th = []
                    for s in range(S):
                        tmp_5th = []
                        for t in range(T):
                            tmp_4th = []
                            for u in range(U):
                                tmp_3rd = []
                                for v in range(V):
                                    tmp_2nd = []
                                    for w in range(W):
                                        lst = list(map(int, input().split()))
                                        print(n, o)
                                        for m in range(M):
                                            if lst[m] == 0:
                                                putt_tomato += 1
                                            elif lst[m] == 1:
                                                q_tomato.append((n, o, p, q, r, s, t, u, v, w, m)) # m만 맨 뒤로 가야함!
                                                q_depth.append(0)
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
    print(1)
else:
    d = 0
    print(q_tomato)
    while q_tomato:
        n, o, p, q, r, s, t, u, v, w, m = q_tomato.popleft()
        d = q_depth.popleft()
        for di in range(22):
            nn, no, np, nq, nr, ns, nt, nu, nv, nw, nm = (
                n + dn[di], o + do[di], p + dp[di], q + dq[di],
                r + dr[di], s + ds[di], t + dt[di], u + du[di],
                v + dv[di], w + dw[di], m + dm[di]
            )
            #print(nn, no, nm)
            if boundary(nn, no, np, nq, nr, ns, nt, nu, nv, nw, nm) and lst_11th[nn][no][np][nq][nr][ns][nt][nu][nv][nw][nm] == 0:
                putt_tomato -= 1
                lst_11th[nn][no][np][nq][nr][ns][nt][nu][nv][nw][nm] = 1
                q_tomato.append((nn, no, np, nq, nr, ns, nt, nu, nv, nw, nm))
                q_depth.append(d + 1)
        print(d, lst_11th)
    print(d) if putt_tomato == 0 else print(-1)