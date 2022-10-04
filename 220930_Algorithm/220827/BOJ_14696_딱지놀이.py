import sys
input = sys.stdin.readline

n = int(input())
for r in range(n):

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_ddagji, b_ddagji = [0] * 5, [0] * 5

    for idx, val in enumerate(a[1:]):
        a_ddagji[val] += 1
    for idx, val in enumerate(b[1:]):
        b_ddagji[val] += 1

    winner = 'D'
    for i in range(4, 0, -1):
        if a_ddagji[i] > b_ddagji[i]:
            winner = 'A'
            break
        elif a_ddagji[i] < b_ddagji[i]:
            winner = 'B'
            break

    print(winner)