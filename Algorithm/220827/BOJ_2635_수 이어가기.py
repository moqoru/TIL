import sys
input = sys.stdin.readline

n = int(input())
ans = []
max_len = 0

for i in range(1, n + 1):
    lst = [n, i]
    while True:
        lst.append(lst[-2] - lst[-1])
        if lst[-1] < 0:
            if max_len < len(lst) - 1:
                max_len = len(lst) - 1
                ans = lst[:-1]
            break

print(max_len)
print(*ans)