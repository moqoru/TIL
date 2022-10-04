import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
# 5일 때는 +-4, 6일 때도 +-4가 나올 방법이 없을까?
odd_n = n - 2 + (n % 2)
even_n = n - 1 - (n % 2)

# 홀수 열, \ 방향
odd_line1, odd_line2 = 0, 0
for i in range(-odd_n, odd_n + 1, 2):
    odd_chk1, odd_chk2 = False, False
    for j in range(-odd_n, odd_n + 2):
        if 0 <= j < n and 0 <= i + j < n:
            # print(j, i + j)
            if lst[j][i + j]: # 1이라면
                odd_chk1 = True
            if lst[i + j][j]:
                odd_chk2 = True
    # print()
    if odd_chk1:
        odd_line1 += 1
    if odd_chk2:
        odd_line2 += 1

even_line1, even_line2 = 0, 0
for i in range(-even_n, even_n + 1, 2):
    even_chk1, even_chk2 = False, False
    for j in range(-even_n, even_n + 2):
        if 0 <= j < n and 0 <= i + j < n:
            # print(j, i + j)
            if lst[j][i + j]: # 1이라면
                even_chk1 = True
            if lst[i + j][j]:
                even_chk2 = True
    # print()
    if even_chk1:
        even_line1 += 1
    if even_chk2:
        even_line2 += 1


print(odd_line1, odd_line2, even_line1, even_line2)
if odd_line1 + odd_line2 == 0:
    print(even_line1 + even_line2)
elif even_line1 + even_line2 == 0:
    print(odd_line1 + odd_line2)
else:
    print(min(odd_line1 + odd_line2, even_line1 + even_line2))