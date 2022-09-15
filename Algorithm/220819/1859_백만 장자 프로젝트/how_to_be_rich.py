import sys
sys.stdin = open('input.txt')

t = int(input())
for cs in range(t):

    n = int(input())
    lst = list(map(int, input().split()))
    profit = 0

    max_tmp = lst[-1]                       # 임시 최대값을 리스트 맨 뒤의 값으로 저장
                                            # 임시 최대값 = 주식 판매하는 날
    for i in range(n - 2, -1, -1):          # 맨 뒤부터 역순으로 탐색
        if lst[i] > max_tmp:                # 새로운 최대값을 찾았다면
            max_tmp = lst[i]                # 최대값 갱신
        else:                               # 아니라면
            profit += max_tmp - lst[i]      # 그날 주식을 사서 임시 최대값에 맞춰 판매하도록 함

    print(f'#{cs + 1} {profit}')