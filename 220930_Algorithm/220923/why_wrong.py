import copy
n = 3
lst = [[0] * n for _ in range(n)]
ans = []

def why_wrong(dep):
    if dep == n ** 2:
        ans.append(copy.deepcopy(lst))
    else:
        lst[dep//n][dep%n] = 1
        why_wrong(dep + 1)
        lst[dep//n][dep%n] = 0
        why_wrong(dep + 1)

why_wrong(0)
print(len(ans))