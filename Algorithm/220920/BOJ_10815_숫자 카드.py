import sys
input = sys.stdin.readline

n = int(input())
lst_n = list(map(int, input().split()))
set_n = set(lst_n)
m = int(input())
lst_m = list(map(int, input().split()))

for i in range(m):
    if set_n & {lst_m[i]}:
        print(1, end = ' ')
    else:
        print(0, end = ' ')