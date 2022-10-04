import sys
sys.stdin = open('input.txt')

for cases in range (1, 11):

    dump = int(input())
    boxes = list(map(int, input().split()))

    box_max, box_min = 0, 101                           # 상자탑 최대, 최소 높이 초기화
    boxes_sorted = [0] * 101                            # 계산 편의를 위해 b_s[100]까지 지정하여 초기화
    for i in boxes:                                     # 정렬 없이 풀기는 어렵다고 생각함, 카운팅 소트 활용
        boxes_sorted[i] += 1                            # 높이 n인 상자탑의 갯수 x를 b_s[n] = x 식으로 저장
        if box_max < i :                                # 상자탑 높이의 최대, 최소값을 트래킹하도록 함.
            box_max = i
        if box_min > i :
            box_min = i

    for move in range(dump):

        boxes_sorted[box_min] -= 1                      # 최대 높이의 상자탑에서 최소 높이의 상자탑으로 1개 옮김
        boxes_sorted[box_min + 1] += 1                  # 높이가 1칸씩 변하므로 b_s 리스트의 옆 칸에 반영
        boxes_sorted[box_max] -= 1
        boxes_sorted[box_max - 1] += 1

        if boxes_sorted[box_min] <= 0:                  # 상자탑의 최소 높이가 더 높아진 경우
            box_min += 1                                # 박스 높이는 1칸씩 높아지므로 최소 높이를 1만 높이면 끝

        if boxes_sorted[box_max] <= 0:                  # 상자탑의 최대 높이가 더 낮아진 경우, 위와 동일
            box_max -= 1

        how_flat = box_max - box_min                    # 최대 높이와 최소 높이의 차이
        if how_flat < 2:                                # 중요! 높이 차이의 최소값은 0 아니면 1일 수밖에 없음!
            break                                       # 높이차가 1인 경우 : 박스를 더 옮겨도 0이 될 수 없음.

    print(f'#{cases} {how_flat}')                       # 높이차 출력