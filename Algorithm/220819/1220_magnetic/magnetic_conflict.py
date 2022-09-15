import sys
sys.stdin = open('input.txt')

for cs in range(10):
    s = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    # 핵심 : 세로줄을 위부터 아래로 탐색, 빨간색 다음에 파란색이 나오면, 교착 상태의 개수를 1씩 늘림
    # 빨강 + 파랑의 1개 쌍마다 1개씩 늘어나므로, 빨강 2 + 파랑 3 같은 경우라도 1개로 처리
    cnt = 0                                     # 교착 상태 개수
    for j in range(100):                        # 한 개의 세로줄 안에서 탐색

        stick = False                           # 파랑에 붙을 빨강이 있는지 기록해두는 변수
        for i in range(100):                    # 가로줄 0번부터 99번까지 순차 탐색

            if lst[i][j] == 1 and not stick:    # 빨강을 발견했고 앞에서 교착상태를 준비할 다른 빨강이 없었다면
                stick = True                    # 교착 상태 준비, 붙을 빨강이 있다고 기록해 둠

            elif lst[i][j] == 2 and stick:      # 파랑을 발견했고 위에 달라붙을 빨강이 있었다면
                stick = False                   # 다음 교착상태를 찾기 위해 변수값을 되돌림
                cnt += 1                        # 교착 상태 개수 증가

    print(f'#{cs + 1} {cnt}')