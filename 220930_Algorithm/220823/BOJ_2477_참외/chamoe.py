import sys
input = sys.stdin.readline

# 케이스 1 : 방향이 423131 => 사이에 끼어 있는 '13'이 파내야 하는 작은 사각형, 안 겹치는 '42'가 큰 사각형
# 케이스 2 : 방향이 142313 => 맨 뒤에 있는 '13'이 파내야 하는 작은 사각형, 안 겹치는 '42'가 큰 사각형
# 따라서 1번 나온 방향이 큰 사각형이 되고, 2번 나온 방향 중 1번 나온 방향과 '정 반대편'에 있는 길이가 파내야 하는 작은 사각형의 너비가 됨

k = int(input())
dirc, wide = [], []                     # 측정 방향과 길이 저장
how_many = [0] * 5                      # 방향별 입력 받은 횟수 저장
exchange = False

for i in range(6):
    d, w = map(int, input().split())
    dirc.append(d)
    wide.append(w)
    how_many[d] += 1

big, smol = 1, 1                        # 큰 사각형과 파내야 하는 작은 사각형
for i in range(1, 5):
    if how_many[i] == 1:                # 1번만 나온 방향을 찾으면...
        idx = dirc.index(i)
        big *= wide[idx]                # 그 방향의 측정된 길이가 큰 사각형의 한 변의 길이
        smol *= wide[(idx + 3) % 6]     # '정 반대편'의 위치에 저장된 길이가 작은 사각형의 한 변의 길이

print((big - smol) * k)                 # 큰 사각형 - 작은 사각형에 밀도를 곱한게 정답