import sys
sys.stdin = open("input.txt")

def prim(node):
    mst_linked = [0] * (V + 1)
    least_far = [11] * (V + 1) # 각 정점별로 MST에 있는 노드와 연결할 수 있는 거리 중 가장 가까운 거리
    least_far[node] = 0 # 0과 0을 연결했으니 그냥 0
    for _ in range(V + 1):
        min_far = 11
        for i in range(V + 1): # 전체 정점 전부 탐색
            if mst_linked[i] == 0 and least_far[i] < min_far:
                new_link = i
                min_far = least_far[i]
        mst_linked[new_link] = 1
        for i in range(E):
            start, end, length = lst[i]
            if start == new_link and mst_linked[end] == 0:
                least_far[end] = min(least_far[end], length)
            elif end == new_link and mst_linked[start] == 0:
                least_far[start] = min(least_far[start], length)
    return sum(least_far)

t = int(input())
for cs in range(t):
    V, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    print(f'#{cs + 1} {prim(0)}')

