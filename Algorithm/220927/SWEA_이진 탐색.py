import sys
sys.stdin = open('input.txt')

def bin_search(l, r, t, prev):
    m = (l + r) // 2
    if b_lst[t] == a_lst[m]:
        return 1
    elif b_lst[t] < a_lst[m]:
        if prev == -1:
            return 0
        bin_search(l, m - 1, t, -1)
    else:
        if prev == 1:
            return 0
        bin_search(m + 1, r, t, 1)
    return 0

t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        ans += bin_search(0, n - 1, i, 0)
    print(f'#{cs + 1} {ans}')