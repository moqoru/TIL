from collections import deque


# import sys
# sys.stdin = open("input.txt")

def new_num(num, func):
    if func == 1:
        check = num + 1
    elif func == 2:
        check = num - 1
    elif func == 3:
        check = num * 2
    else:
        check = num - 10
    if 1 <= check <= 1000000 and lst[check] == -1:
        lst[check] = lst[num] + 1
        if check == m:
            return True
        q.append(check)
    return False


t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    lst = [-1] * 1000001
    lst[n] = 0
    q = deque([n])
    while q:
        now = q.popleft()
        for i in range(4):
            if new_num(now, i):
                print(f'#{cs + 1} {lst[m]}')
                break