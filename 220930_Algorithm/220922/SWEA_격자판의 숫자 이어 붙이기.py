import sys
sys.stdin = open('input.txt')

# 가지치기를 하고 싶지만 함부로 백트래킹을 하기는 어려운 문제...
# 예를 들어, 특정 2곳의 위치에서 똑같이 '111'의 조합이 나왔다고 한들,
# 그 2곳에서 주변 4방향의 숫자까지 전부 같으리라는 보장이 없다!
# 시작점이 다르면 거의 항상 문자열 조합이 다르게 나와서, 완탐 이외에는 방법이 없을 지도?
# 좌표를 일일이 저장하면 될지도 모르겠지만, 글쎄... 그거 저장하고 판별하는데 시간이 더 걸리지 않으려나?

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def dfs(x, y, dep):
    if dep == 7:
        if stk[-1] not in ans:
            ans.add(stk[-1])
    else:
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if 0 <= nx < 4 and 0 <= ny < 4:
                stk.append(stk[-1] * 10 + lst[nx][ny])
                dfs(nx, ny, dep + 1)
                stk.pop()

t = int(input())
for cs in range(t):
    lst = [list(map(int, input().split())) for _ in range(4)]
    stk, ans = [], set()
    for i in range(4):
        for j in range(4):
            stk.append(lst[i][j])
            dfs(i, j, 1)
            stk.pop()
    print(f'#{cs + 1} {len(ans)}')