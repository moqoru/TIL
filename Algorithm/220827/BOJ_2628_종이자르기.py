import sys
input = sys.stdin.readline

x, y = map(int, input().split())
x_cut, y_cut = [0, x], [0, y]               # 시작과 끝 지점을 먼저 리스트에 넣습니다.
n = int(input())

for i in range(n):

    d, l = map(int, input().split())        # 자르는 위치를 가로, 세로 각각 따로 리스트에 저장합니다.

    if d == 1:
        x_cut.append(l)
    else:
        y_cut.append(l)

x_cut.sort()                                # 정렬해주면 시작과 끝 지점을 포함해,
y_cut.sort()                                # 잘린 부분 위치가 담긴 리스트가 완성됩니다.
x_max, y_max = 0, 0

for idx, val in enumerate(x_cut[1:]):       # 이제 잘린 부분 앞뒤의 차이를 계산해서 이 값이 최대가 될 때를 찾습니다.

    if x_max < val - x_cut[idx]:            # index slicing과 enumerate를 모두 활용했으므로, 리스트 위치 참조 주의!
        x_max = val - x_cut[idx]

for idx, val in enumerate(y_cut[1:]):       # 가로와 세로 모두 최대값을 찾은 후 서로 곱하면 가장 큰 조각의 넓이입니다!

    if y_max < val - y_cut[idx]:
        y_max = val - y_cut[idx]

print(x_max * y_max)