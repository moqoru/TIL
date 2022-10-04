import sys
sys.stdin = open('input.txt')

# 시작 시간을 기준으로 정렬하면 안 되는 이유...?
# 빨리 '끝나는' 작업을 먼저 진행해야 다음 작업을 조금이라도 더 많이 할 수 있다!!!
t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x: (x[1]))
    time, ans = 0, 0
    for i in range(n):
        if lst[i][0] >= time:
            ans += 1
            time = lst[i][1]
    print(f'#{cs + 1} {ans}')