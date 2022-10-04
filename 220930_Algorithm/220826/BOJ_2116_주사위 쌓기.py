# 맨 밑의 주사위의 놓는 방향을 결정하면 그 위의 주사위들은 순서대로 쌓기만 하면 되니, 추가적인 경우의 수가 없다!?
# 결국 경우의 수는 단 6가지, 맨 밑의 주사위를 어떻게 놓는가에 대해 결정될 뿐이다.
# 그냥 6가지에 대해 옆면의 합 최대치를 계산해보면 끝!

import sys
input = sys.stdin.readline

def dice_max(t, b):                                             # 주사위의 옆면 값의 최대치를 알려주는 함수
    if 6 not in (t, b):                                         # 윗면, 아랫면 중 어느 쪽이라도 6이 없으면 최대값은 6
        return 6
    elif 5 not in (t, b):                                       # 어느 한 면에 6이 있지만 다른 면이 5가 아니면 최대값은 5
        return 5
    else:                                                       # 윗면, 아랫면이 둘 다 5, 6이라면 최대값은 4
        return 4

dice_oppo = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}                # 주사위의 각 위치에 대해 반대편 위치는 어디인지 알려주는 딕셔너리

n = int(input())
dice_lst = [list(map(int, input().split())) for _ in range(n)]
side_max = 0                                                    # 옆면의 합 최대치

for i in range(6):                                              # 밑바닥의 주사위를 어떻게 놓을지의 경우의 수 6가지만 따지면 끝

    top_prev = dice_lst[0][i]                                   # 밑바닥의 주사위의 윗면의 숫자
    bottom_prev = dice_lst[0][dice_oppo[i]]                     # 밑바닥의 주사위의 아랫면의 숫자
    side_sum = dice_max(top_prev, bottom_prev)                  # 옆면의 숫자들 중 가장 큰 숫자를 옆면의 합으로 더해 줌

    for j in range(1, n):                                       # 그 위로 쌓는 주사위는 순서대로 숫자 겹쳐서 쌓아보기

        bottom_now = top_prev                                   # 위에 올리는 주사위의 아랫면과 밑의 주사위의 윗면의 숫자는 같음
        bottom_idx = dice_lst[j].index(top_prev)                # 아랫면의 위치를 확인한 후
        top_now = dice_lst[j][dice_oppo[bottom_idx]]            # 윗면의 값도 기록해 줌

        side_sum += dice_max(top_now, bottom_now)               # 옆면의 숫자들 중 가장 큰 숫자를 옆면의 합으로 더해 줌

        top_prev = top_now                                      # 그 다음 단계를 계산하기 위해 지금 쌓았던 주사위의 윗면의 값을 옮겨 줌
        # bottom_prev = bottom_now                              # 사실 아랫면은 계산할 필요도 없음!

    if side_max < side_sum:                                     # 최대값 갱신
        side_max = side_sum

print(side_max)
