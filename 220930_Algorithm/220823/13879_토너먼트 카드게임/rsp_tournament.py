import sys
sys.stdin = open('sample_input(2).txt')

# 3(보)>2(바위), 2(바위)>1(가위), 1(가위)>3(보)

def rsp(lst, front, back):                              # 가위바위보 승패 판정 함수
                                                        # 앞사람이 이기면 -1, 뒷사람이 이기면 1, 비기면 0을 리턴
    if lst[front] == 1:                                 # 앞사람이 1(가위)
        if lst[back] == 1:                              # 뒷사람이 1(가위) => 비김
            return 0
        elif lst[back] == 2:                            # 뒷사람이 2(바위) => 뒷사람 승리
            return 1
        else:                                           # 뒷사람이 3(보) => 앞사람 승리
            return -1

    elif lst[front] == 2:                               # 앞사람이 2(바위)
        if lst[back] == 1:                              # 뒷사람이 1(가위) => 앞사람 승리
            return -1
        elif lst[back] == 2:                            # 뒷사람이 2(바위) => 비김
            return 0
        else:                                           # 뒷사람이 3(보) => 뒷사람 승리
            return 1

    else:                                               # 앞사람이 3(보)
        if lst[back] == 1:                              # 뒷사람이 1(가위) => 뒷사람 승리
            return 1
        elif lst[back] == 2:                            # 뒷사람이 2(바위) => 앞사람 승리
            return -1
        else:                                           # 뒷사람이 3(보) => 비김
            return 0

def d_n_c(lst, front, back, winner):                    # 분할 정복 함수

    mid = (front + back) // 2                           # 중앙 지점의 위치 계산

    if front == mid:                                    # 분할한 영역 안에 2명 혹은 1명밖에 없다면
        judge = rsp(lst, front, back)                   # 영역 안의 사람끼리 가위바위보 판정
        winner = back if judge == 1 else front          # 뒷사람이 이기면 뒷사람을 승자로 저장, 비기거나 앞사람이 이기면 앞사람을 승자로 저장

    else:                                               # 아직 영역을 더 분할할 수 있다면
        l_winner = d_n_c(lst, front, mid, winner)       # 왼쪽 영역의 승자와 오른쪽 영역의 승자를 재귀함수로 따로 호출
        r_winner = d_n_c(lst, mid + 1, back, winner)
        judge = rsp(lst, l_winner, r_winner)            # 영역별 승자끼리 가위바위보 판정
        winner = r_winner if judge == 1 else l_winner   # 마찬가지로 승자를 갱신함

    return winner                                       # 최종 승자의 위치 리턴

t = int(input())
for cs in range(t):

    n = int(input())
    lst = [0] + list(map(int, input().split()))         # 번호가 1부터 n까지이므로 맨 앞에 0 하나를 더 붙임
    ans = d_n_c(lst, 1, n, 0)                           # 가위바위보 카드 정보, 시작 위치, 끝 위치, 승자 정보 넣어서 분할정복 함수 호출
    print(f'#{cs + 1} {ans}')                           # 승자 출력



    min()