import sys
sys.stdin = open("input.txt")

# 예시 코드 복붙.
def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

# Skewed Tree가 만들어져서 탐색하기는 안 좋아 질지도...?
# 제대로 쓰려면 rank를 활용해야 함
def union(x, y):
    parent[find_set(y)] = find_set(x)

t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    lst = list(map(int, input().split()))
    ans_set = set()
    for i in range(0, m * 2, 2):
        union(lst[i], lst[i + 1])
    for i in range(1, n + 1):
        ans_set.add(find_set(i))
    print(f'#{cs + 1} {len(ans_set)}')