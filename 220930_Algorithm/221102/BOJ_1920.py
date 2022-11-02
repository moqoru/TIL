import sys
input = sys.stdin.readline

N = int(input())
Origin = list(map(int, input().split()))
M = int(input())
Search = list(map(int, input().split()))

for i in range(M):
    print(1) if Search[i] in Origin else print(0)