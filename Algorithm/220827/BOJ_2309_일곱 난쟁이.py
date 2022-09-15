import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(9)]
lst.sort()
sum_height = sum(lst)
found = False

for i in range(9):
    for j in range(i + 1, 9):
        if sum_height - (lst[i] + lst[j]) == 100:
            for k in range(9):
                if k not in (i, j):
                    print(lst[k])
            found = True
            break
    if found:
        break
