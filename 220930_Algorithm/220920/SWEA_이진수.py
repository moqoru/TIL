import sys
sys.stdin = open("input.txt")

t = int(input())
for cs in range(t):
    n, hexa = input().split()
    ans = ""

    for i in range(int(n)):
        ans += bin(int("0x" + hexa[i], 16))[2:].zfill(4)

    print(f'#{cs + 1} {ans}')