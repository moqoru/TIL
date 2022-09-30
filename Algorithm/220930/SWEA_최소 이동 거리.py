import sys
sys.stdin = open("input.txt")

def dijkstra(s):
    # 현재까지 연결된 노드 정보를 전부 저장해 둠.
    U = {s}
    # 도착점마다 시작점에서 갈 수 있는 최소 거리를 기록함.
    distance = [999999] * (V + 1)
    distance[s] = 0 # 시작점 => 시작점 거리는 당연히 0.

    # graph_di는 시작점 인덱스 : (도착점, 거리)로 저장됐었음.
    # 먼저 '맨 처음 시작점 기준'으로 갈 수 있는 모든 도착점에 대해 간선 정보 기록
    for e, w in graph_di[s]:
        distance[e] = w

    # 순서는 제각각이지만, 정확히 노드 갯수만큼 수행해서 연결될 예정임
    for _ in range(V):
        # 연결된 노드들에서 갈 수 있는, 간선 길이의 최소값을 저장할 예정
        min_val = 999999
        # 모든 간선에 대해, 연결되지 않은 노드이고 길이가 더 짧다면 간선과 노드 번호 기록
        for i in range(V + 1):
            if i not in U and min_val > distance[i]:
                min_val = distance[i]
                idx = i
        # 찾은 노드를 연결
        U.add(idx)
        # 연결한 노드를 바탕으로 모든 도착점들에 대해 시작점과의 거리의 최소값을 갱신
        for e, w in graph_di[idx]:
            distance[e] = min(distance[e], distance[idx] + w)

    # 이 문제는 도착점이 간선의 끝번호이므로 도착점의 distance 값을 출력하면 끝!
    return distance[V]

t = int(input())
for cs in range(t):
    # 간선의 끝번호 (0부터 시작), 간선의 갯수
    V, E = map(int, input().split())
    graph_di = [[] for _ in range(V + 1)]
    for _ in range(E):
        # 간선의 시작점, 끝점, 거리를 받아옴
        start, end, weight = map(int, input().split())
        # 각 시작점마다 갈 수 있는 도착점 + 거리 정보를 2차원 리스트?로 기록해 둠.
        graph_di[start].append((end, weight))

    print(f'#{cs + 1} {dijkstra(0)}')