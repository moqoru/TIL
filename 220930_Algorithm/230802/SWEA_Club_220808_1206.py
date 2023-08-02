import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

for cs in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, n - 2):
        light = lst[i]
        for j in range(i - 2, i):
            light = min(lst[i] - lst[j], light)
        for j in range(i + 1, i + 3):
            light = min(lst[i] - lst[j], light)
        if light > 0:
            ans += light
    print(f'#{cs + 1} {ans}')