import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
jul = [1]

for i in range(1, n):
    jul = jul[:i - lst[i]] + [i + 1] + jul[i - lst[i]:]

print(*jul)
