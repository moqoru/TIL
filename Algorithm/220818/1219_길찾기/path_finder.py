import sys
sys.stdin = open('input.txt')

for cs in range(10):                        # 스택 이용한 DFS 탐색법 풀이

    t, p = map(int, input().split())        # 케이스 번호, 길 갯수
    path_1 = [-1] * 100                     # 도착 번호 저장 리스트 1, 도착점이 0일 수도 있으므로 -1로 초기화
    path_2 = [-1] * 100                     # 도착 번호 저장 리스트 2
    lst = list(map(int, input().split()))

    for i in range(0, p * 2, 2):            # 데이터 길이가 길 갯수의 2배이므로 step을 2로 잡음
        a, b = lst[i], lst[i + 1]           # 시작, 도착 정점 정보 읽음
        if path_1[a] == -1:                 # 리스트 1에 저장 가능하면
            path_1[a] = b                   # 시작점 위치에 도착점 정보 기록
        else:                               # 리스트 1에 값이 들어있다면 리스트 2에 기록
            path_2[a] = b

    cur = 0                                 # 현재 위치
    stack = []                              # 스택
    while cur != 99:                        # 도착점에 갈 때까지 루프

        if path_2[cur] != -1:               # 경로 리스트 2에 갈 수 있는 길이 있다면
            stack.append(path_2[cur])       # 스택에 경로를 삽입하고 (도착점만 저장해도 충분함)
            path_2[cur] = -1                # 그 길을 지움 (순환 경로가 있을 경우 무한 루프되는 것을 방지)
        if path_1[cur] != -1:               # 경로 리스트 1도 마찬가지로 체크해서 스택에 삽입
            stack.append(path_1[cur])       # (stack pop은 나중에 넣은 게 먼저 나오므로 1을 나중에 넣도록 바꿈)
            path_1[cur] = -1

        if len(stack) < 1:                  # 스택이 비어있다면 = 갈 수 있는 길이 없다면
            cur = 0                         # 시작점으로 되돌리고 종료
            break
        else:                               # 갈 수 있는 길이 있다면
            cur = stack.pop()               # 스택을 pop해서 cur에 다음 탐색 위치 기록

    # 사실 현재 위치에서 갈 수 있는 길이 없다면 길이 있을 때까지 한 칸씩 왔던 길을 되돌아가야 하는데,
    # 이건 그냥 stack pop만 해서 지나왔던 경로 중 갈 수 있었던 또 다른 길로 한번에 되돌아가게 풀었음
    # 시간상으론 효율적이지만 사람이 분석하기에는 어려운 코드라고 생각...
    # 왔던 경로를 지워버리므로 여러 경로를 모두 찾아야 하는 경우에도 곤란할 수 있음

    if cur:                                 # cur가 99라면 도착했다는 의미이므로
        print(f'#{t} 1')                    # 경로가 있다고 출력
    else:                                   # cur가 0이라면 못 도착했다는 의미이므로
        print(f'#{t} 0')                    # 경로가 없다고 출력