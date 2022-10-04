import sys
import collections
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
slice_sum = 0
q = collections.deque()

for idx, val in enumerate(lst[:k]):
    slice_sum += val

ans_max = slice_sum

for idx, val in enumerate(lst[k:]):
    slice_sum += val - lst[idx]
    ans_max = max(ans_max, slice_sum)
print(ans_max)

