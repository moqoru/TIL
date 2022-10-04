# import sys
# sys.stdin = open('input.txt')

t = int(input())
for cs in range(t):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst_csort = [0] * 11112
    last_order = 0
    boong_fish = 0

    for idx in lst:
        lst_csort[idx] += 1
        if idx > last_order:
            last_order = idx

    for i in range(last_order + 1):
        if i % m == 0 and i > 0:
            boong_fish += k
        if lst_csort[i] != 0:
            if boong_fish >= lst_csort[i]:
                boong_fish -= lst_csort[i]
            else:
                boong_fish = -1
                break

    if boong_fish == -1:
        print(f'#{cs + 1} Impossible')
    else:
        print(f'#{cs + 1} Possible')