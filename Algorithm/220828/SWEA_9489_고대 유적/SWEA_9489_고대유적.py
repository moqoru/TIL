import sys
sys.stdin = open('input1.txt')

t = int(input())
for cs in range(t):
    n, m = map(int, input().split())                            # 입력
    lst = [list(map(int, input().split())) for _ in range(n)]

    line_max = 0                                                # 한 줄 최대 길이

    for i in range(n):                                          # 가로 방향의 줄의 길이 탐색
        line_cnt = 0                                            # 현재 줄의 길이

        for j in range(m):

            if lst[i][j]:                                       # 현재 칸이 1이라면
                line_cnt += 1                                   # 현재 줄의 길이 증가

            else:                                               # 0이라면
                line_max = max(line_max, line_cnt)              # 한 줄의 최대 길이를 갱신하고
                line_cnt = 0                                    # 현재 줄의 길이를 리셋

        line_max = max(line_max, line_cnt)                      # 루프가 끝난 뒤 한번 더 최대 길이 갱신

    for j in range(m):                                          # 세로 방향으로 한 번 더 탐색
        line_cnt = 0

        for i in range(n):

            if lst[i][j]:
                line_cnt += 1
                
            else:
                line_max = max(line_max, line_cnt)
                line_cnt = 0

        line_max = max(line_max, line_cnt)

    print(f'#{cs + 1} {line_max}')                              # 최대 길이 출력