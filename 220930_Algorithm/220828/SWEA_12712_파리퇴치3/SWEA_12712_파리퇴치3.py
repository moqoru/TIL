import sys
sys.stdin = open('in1.txt')

dx = (1, -1, 0, 0, 1, 1, -1, -1)                                # 델타 탐색
dy = (0, 0, 1, -1, 1, -1, 1, -1)                                # 0~3번은 십자, 4~7번은 X자 탐색

t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]

    fly_max = 0                                                 # 잡힌 파리의 최대치
    for i in range(n):                                          # i, j는 스프레이를 뿌리는 중심 지점
        for j in range(n):
                                                                # 먼저 십자 방향부터 시작함
            fly_catch = fly[i][j]                               # 중심 지점의 파리를 우선 잡은 파리 마릿수로 넣음
            for r in range(1, m):                               # 길이 m만큼 탐색, 범위 주의!
                for d in range(4):                              # 4방향 델타 탐색

                    ni, nj = i + dx[d] * r, j + dy[d] * r       # 중심점에서 각 방향별로 r 만큼의 길이를 갔을 때
                    if 0 <= ni < n and 0 <= nj < n:             # 만약 리스트 밖으로 벗어나지 않았다면
                        fly_catch += fly[ni][nj]                # 잡은 파리 마릿수 추가

            fly_max = max(fly_max, fly_catch)                   # 파리 최대 마릿수 갱신
                                                                # 중심점을 유지한 채 X자 방향도 탐색
            fly_catch = fly[i][j]
            for r in range(1, m):
                for d in range(4, 8):                           # X자 방향 델타 탐색, 이 부분 제외하고는 십자 부분 코드와 등일

                    ni, nj = i + dx[d] * r, j + dy[d] * r
                    if 0 <= ni < n and 0 <= nj < n:
                        fly_catch += fly[ni][nj]

            fly_max = max(fly_max, fly_catch)

    print(f'#{cs + 1} {fly_max}')