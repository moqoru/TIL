n, m = map(int, input().split())
ans = 0
for i in range(n):
    lst = list(map(int, input().split()))
    ans = max(ans, min(lst))
print(ans)