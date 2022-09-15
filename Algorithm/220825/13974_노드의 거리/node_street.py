import sys
sys.stdin = open('sample_input(3).txt')
from collections import deque

t = int(input())
for cs in range(t):

    v, e = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())

    depth, found = 1, 0                                     # depth는 탐색한 깊이, found는 경로를 찾았는지 여부
    visited = set([s])                                      # 탐색한 노드의 정보를 저장
    q_now = deque([s])                                      # 현재 탐색 깊이에서 방문 가능한 노드가 담긴 큐
    q_next = deque()                                        # 다음 단계 탐색에서 방문 가능한 노드

    while q_now:                                            # 현재 깊이에서 갈 수 있는 노드가 남아 있다면

        cur = q_now.popleft()                               # 탐색할 노드를 dequeue

        for idx in lst:                                     # 간선들의 정보를 탐색

            if idx[0] == cur and idx[1] not in visited:     # 간선의 시작점이 현재 탐색하는 노드이고 도착점이 방문한 적 없는 노드라면

                if idx[1] == g:                             # 도착점을 찾았다면 바로 break
                    found = 1
                    break

                else:                                       # 아니라면 다음 단계 큐에 enqueue하고 방문 정보 기록
                    q_next.append(idx[1])
                    visited.add(idx[1])

            elif idx[1] == cur and idx[0] not in visited:   # 노드의 방향성이 없으므로 시작점과 도착점을 반대로도 체크

                if idx[0] == g:
                    found = 1
                    break

                else:
                    q_next.append(idx[0])
                    visited.add(idx[0])

        if found:                                           # 경로 찾았으면 더 루프 돌 필요 없음
            break

        elif not q_now:                                     # 현재 깊이의 노드 탐색이 모두 끝났다면
            q_now, q_next = q_next, q_now                   # 다음 단계 노드 탐색을 시작함
            # q_now = q_next.copy()                         # 위 swap 구문은 이하 2줄짜리 구문과 동일한 기능
            # q_next.clear()                                # swap을 쓰면 얕은 복사로 골머리 앓을 필요 없이 바로 교환 가능
            depth += 1                                      # 탐색 깊이를 1 증가

    if found:                                               # 경로가 존재한다면
        print(f'#{cs + 1} {depth}')                         # 탐색 깊이가 곧 노드의 거리와 동일함
    else:                                                   # 존재하지 않으면 0 출력, found에 어차피 0 저장되어 있을 것임
        print(f'#{cs + 1} {found}')