import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p += t
q += t

if p // w % 2 == 1:
    p = w - p % w
else:
    p %= w
if q // h % 2 == 1:
    q = h - q % h
else:
    q %= h

print(p, q)