import sys
sys.stdin = open('1.txt')
t = int(input())
for cases in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    num_max, num_min = 0, 1000001
    for val in lst:
        if val > num_max :
            num_max = val
        if val < num_min :
            num_min = val
    print(f'#{cases} {num_max - num_min}')