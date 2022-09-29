def prim(node):
    mst = [0] * (V + 1)  # idx 번째 위치의 노드가 연결이 됐는지 여부 기록
    key = [float('inf')] * (V + 1)  # 갱신이 안됐으면 무한대 값이 들어있을 것.
    parent = [-1] * (V + 1)  # idx 번째 위치의 노드의 부모가 어느 노드인지 기록
    key[node] = 0  # 시작점의 노드만 0으로 기록
    for _ in range(V + 1):
        min_val = float('inf')

        # ...연결된 점 중에서 최소값을 찾는 것 아닌가...???????
        # 어차피 mst가 0인 점은 루프 한번당 한번 아닌가...??????
        for i in range(V + 1):  # 모든 정점을 훑어서...
            if mst[i] == 0 and key[i] < min_val:  # 연결 안 된 점이고,
                s = i  # 새로 연결할 점
                min_val = key[i]  # 최소값을 키값으로 갱신
        mst[s] = 1  # 연결되었는가?

        for e in range(V + 1):
            if mst[e] == 0 and graph_matrix[s][e] > 0:
                if key[e] > graph_matrix[s][e]:
                    key[e] = graph_matrix[s][e]
                    parent[e] = s
    return sum(key)

t = int(input())
for cs in range(t):
    V, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    graph_list = [[] for _ in range(V + 1)]
    graph_matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for start, end, weight in lst:
        graph_list[start].append((end, weight))
        graph_list[end].append((start, weight))
        graph_matrix[start][end] = weight
        graph_matrix[end][start] = weight

    print(prim(0))