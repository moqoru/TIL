import sys
sys.stdin = open("input.txt")

def postorder(cur):                                             # 재귀함수로 풀어냄
    if cur > n:
        return 0                                                # 그래프 범위 밖으로 벗어났으면 0을 리턴 (덧셈에 지장 X)
    elif lst[cur] != 0:
        return lst[cur]                                         # 리프 노드거나 이미 값이 기록됐다면 그 값을 리턴
    else:
        lst[cur] = postorder(cur * 2) + postorder(cur * 2 + 1)  # 부모 노드에 자식 노드의 합을 기록
        return lst[cur]                                         # 부모 노드의 값을 리턴

t = int(input())
for cs in range(t):
    n, m, l = map(int, input().split())
    lst = [0] * (n + 1)
    for i in range(m):
        in_a, in_b = map(int, input().split())
        lst[in_a] = in_b

    postorder(1)
    print(f'#{cs + 1} {lst[l]}')