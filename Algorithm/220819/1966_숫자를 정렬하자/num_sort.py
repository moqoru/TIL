import sys
sys.stdin = open('input.txt')
t = int(input())

for cs in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):                              # 앞에서부터 순차적으로 선택 정렬 진행
        now_min = lst[i]                            # i번째 위치의 값을 임시 최솟값으로 설정함
        idx_min = i                                 # 발견한 최솟값의 위치를 기억할 변수

        for j in range(i + 1, n):                   # 맨 뒤까지 쭉 탐색함
            if lst[j] < now_min:                    # 새로운 최솟값 발견시 갱신
                now_min = lst[j]
                idx_min = j

        lst[idx_min], lst[i] = lst[i], lst[idx_min] # 발견한 최솟값을 i번째 값과 교환함
                                                    # 맨 앞부터 최솟값들이 차례로 쌓이면서 정렬됨
    print(f'#{cs + 1}', end = ' ')
    for i in lst:
        print(f'{i}', end = ' ')
    print()