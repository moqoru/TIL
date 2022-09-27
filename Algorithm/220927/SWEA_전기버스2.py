import sys
sys.stdin = open('input.txt')

# 풀이 1
# 시작점에서 배터리 용량만큼 갈 수 있는 모든 충전소를 탐색, 그 충전소에서 충전한 뒤 배터리 용량을 갱신하여 재귀 호출
# 현재 충전소에서 남은 배터리 용량으로 종점까지 갈 수 있으면 최소 충전 횟수를 갱신
def back_track(stop, charge, fuel):
    global ans
    #print(stop, charge, fuel)
    if stop + fuel >= lst[0]:
        ans = min(ans, charge)
    # 백트래킹 : 현재 충전 횟수가 지금까지 시작점에 도달한 최소 충전 횟수보다 많으면 진행하지 않음.
    elif charge < ans:
        # 갈 수 있는 충전소마다 그 위치로 이동하고 배터리 용량 갱신, 충전 횟수 +1
        for i in range(stop + fuel, stop, -1):
            # 그 정류장에 갔을 때 충전량이 배터리 잔량보다 높을 때만 그 충전소 방문
            if lst[i] > fuel + stop - i:
                back_track(i, charge + 1, lst[i])

# 풀이 2
# 도착점부터 역순으로 정류장을 훑으면서, 특정 충전소의 배터리 용량이 충전소까지의 거리보다 많으면 재귀 호출하도록 함
# 시작점에 도달했다면 최소 충전 횟수를 갱신
# 시간이 더 오래 걸리는 이유는 뭘까?
# def back_track(stop, charge):
#     global ans
#     if stop == 1:
#         ans = min(ans, charge)
#     # 백트래킹 : 현재 충전 횟수가 지금까지 시작점에 도달한 최소 충전 횟수보다 많으면 진행하지 않음.
#     elif charge < ans:
#         # 조건에 맞는 배터리 충전소를 찾아 그 위치로 이동하고 충전 횟수 +1
#         for i in range(stop - 1, 0, -1):
#             if lst[i] >= stop - i:
#                 back_track(i, charge + 1)

t = int(input())
for cs in range(t):
    lst = list(map(int, input().split()))
    ans = lst[0] + 1
    back_track(1, 0, lst[1])
    # 풀이 2의 경우 시작점은 충전 횟수에서 제외하므로 -1에서 시작해야 문제 조건과 일치함
    # back_track(lst[0], -1)
    print(f'#{cs + 1} {ans}')