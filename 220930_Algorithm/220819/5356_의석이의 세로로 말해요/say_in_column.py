import sys
sys.stdin = open('sample_input.txt')
t = int(input())

for cs in range(t):
    lst = [input() for _ in range(5)]
    ans = ''
    max_len = -1

    for i in range(5):                  # 가장 길이가 긴 가로줄 탐색
        if len(lst[i]) > max_len:
            max_len = len(lst[i])       # 가장 긴 길이의 가로줄을 저장하여 그 길이만큼 탐색해야 함

    for j in range(max_len):            # 각각의 가로줄 안에서...
        for i in range(5):              # 5개 세로줄을 탐색하면서 문자열을 붙여 나감
            if len(lst[i]) > j:         # 만약 [i][j]의 위치를 참조할 수 있다면(리스트 밖으로 벗어나지 않으면)
                ans += lst[i][j]        # 해당 위치의 문자열을 붙임
    print(f'#{cs + 1} {ans}')           # 붙인 문자열 출력
