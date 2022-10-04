import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(s):                                     # depth 단계별로 최대값을 갱신해야 하므로 bfs 연산

    q.append(s)                                 # q는 이번 차례에 방문할 노드 번호
    q_dep.append(1)                             # q_dep은 그 노드를 방문할 때의 depth
    max_dep = 1                                 # 가장 많이 들어간 깊이
    max_num = s                                 # 현재 깊이에서의 가장 큰 노드 번호
    graph[s][0] = 1                             # graph에서 각 노드의 첫 번호는 방문 여부, 그 다음부터는 방문할 수 있는 노드 번호가 들어감

    while q:                                    # q가 빌 때까지 연산
        cur = q.popleft()                       # 이번 노드의 번호 pop
        now_dep = q_dep.popleft()               # 탐색 depth를 pop

        if now_dep > max_dep:                   # 탐색 depth가 갱신됐다면 일단 이번 노드 값을 최대값으로 적어둠
            max_dep = now_dep
            max_num = cur
        else:                                   # 같은 depth라면 노드 번호의 최대값을 갱신
            max_num = max(max_num, cur)

        for i in range(1, len(graph[cur])):     # 현재 노드에서 갈 수 있는 노드들을 탐색
            if graph[graph[cur][i]][0] == 0:    # 아직 방문하지 않은 노드라면
                graph[graph[cur][i]][0] = 1     # 방문했다고 표시해주고
                q.append(graph[cur][i])         # enqueue 작업
                q_dep.append(now_dep + 1)

    return max_num                              # 최종 최대값 리턴

for cs in range(10):
    graph = [[0] for _ in range(101)]
    data, start = map(int, input().split())
    lst = list(map(int, input().split()))
    q, q_dep = deque(), deque()

    for i in range(0, data, 2):
        graph[lst[i]].append(lst[i + 1])

    print(f'#{cs + 1} {bfs(start)}')