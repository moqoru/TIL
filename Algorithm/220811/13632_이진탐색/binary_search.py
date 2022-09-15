import sys
sys.stdin = open('sample_input(2).txt')

t = int(input())                                    # 케이스 수 입력받음

for cs in range(1, t + 1):
    p, pa, pb = map(int, input().split())           # 전체 페이지, A의 목표, B의 목표 입력

    pa_l, pa_r = 1, p                               # 1페이지와 끝 페이지로 A, B의 양 끝점 초기화
    pb_l, pb_r = 1, p
    win = 0                                         # 승리 여부 판단

    while not win:                                  # 승부가 나지 않은 경우 = win 값이 안 바뀐 경우에만 루프
        pa_c = int((pa_l + pa_r) / 2)               # 중간 페이지 계산
        pb_c = int((pb_l + pb_r) / 2)
                                                    # 이 부분에서 변수 이름 실수 많이 나옴...
        if pa_c == pa_l:                            # (예외처리!) 하필 왼쪽 + 1 = 오른쪽인 경우 상대방 승리 처리
            win += 2                                # 평균 내봤자 버림 하면 왼쪽 페이지와 계속 같아져서 무한루프가 됨
        elif pa_c == pa:                            # A의 중간 페이지와 A의 목표 페이지가 일치하면
            win += 1                                # A의 승리 기록
        elif pa_c > pa:                             # 중간 페이지가 목표 페이지보다 크다면
            pa_r = pa_c                             # 오른쪽 끝을 중간 페이지로 바꿔서 더 작게 만듦
        else:                                       # ~~ 작다면
            pa_l = pa_c                             # 왼쪽 끝을 중간 페이지로 바꿔서 더 크게 만듦

        if pb_c == pb_l:
            win += 1
        elif pb_c == pb:                            # B의 경우도 동일
            win += 2
        elif pb_c > pb:
            pb_r = pb_c
        else:
            pb_l = pb_c

    if win == 1:                                    # A만 승리했다면
        print(f'#{cs} A')
    elif win == 2:                                  # B만 승리했다면
        print(f'#{cs} B')
    else:                                           # A, B 모두 승리했다면 = 비겼다면
        print(f'#{cs} 0')                           # 둘 다 무한루프에 빠졌을 경우라도 무승부로 들어감
