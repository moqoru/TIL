import sys
sys.stdin = open('input.txt')

# 0부터 n -1 까지 1번씩만 쓰는 순열을 생성하면서 한 자리가 추가될 때마다 생산 비용을 1개 제품씩 추가해 둔다.
# n 길이의 순열을 생성하면 전체 제품의 최소 생산 비용을 갱신해 준다.
def npr(dep, cost):
    global ans
    if dep >= n:
        ans = min(cost, ans)
    # 현재 생산 비용이 이미 최소 생산 비용보다 크면 더이상 탐색하지 않도록 백트래킹 처리.
    elif cost < ans:
        for i in range(n):
            if i not in permu[:dep]:
                permu[dep] = i
                npr(dep + 1, cost + lst[dep][i])

t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    ans = n * 100
    permu = [0] * n
    npr(0, 0)
    print(f'#{cs + 1} {ans}')