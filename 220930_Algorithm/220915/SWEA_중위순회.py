import sys
sys.stdin = open('input.txt')

def inorder(now, end):              # 재귀 구문으로 중위 순회
    if now <= end:
        inorder(now * 2, end)       # 왼쪽, 부모, 오른쪽 순서
        print(lst[now], end='')
        inorder(now * 2 + 1, end)

for cs in range(10):
    n = int(input())
    lst = [0] * (n + 1)
    ans = []
    for i in range(1, n + 1):
        lett = input().split()
        lst[i] = lett[1]

    cur = 1
    while len(ans) < n:
        if lst[cur] == '':
            cur //= 2
        elif cur * 2 <= n and lst[cur * 2] != '':
            cur *= 2
        else:
            ans.append(lst[cur])
            lst[cur] = ''
            if cur * 2 + 1 <= n and lst[cur * 2 + 1] != '':
                cur = cur * 2 + 1
            else:
                cur //= 2
    print(f'#{cs + 1} ', end="")
    for i in range(len(ans)):
        print(ans[i], end="")
    print()
