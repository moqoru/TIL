import sys
input = sys.stdin.readline

girl = [0] * 7
boy = [0] * 7

n, k = map(int, input().split())
for i in range(n):
    s, g = map(int, input().split())
    if s == 0:
        girl[g] += 1
    else:
        boy[g] += 1

ans_sum = 0
for i in range(1, 7):
    ans_sum += (girl[i] + k - 1) // k + (boy[i] + k - 1) // k

print(ans_sum)