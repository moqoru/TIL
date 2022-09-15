import sys
input = sys.stdin.readline

n = int(input())
on_off_lst = list(map(int, input().split()))
st = int(input())
stu_lst = [list(map(int, input().split())) for _ in range(st)]

for i in range(st):

    if stu_lst[i][0] == 1:                                              # 남학생의 경우

        for j in range(stu_lst[i][1] - 1, n, stu_lst[i][1]):            # 인덱스 시작이 0번이므로 시작 번호를 맞추고, step은 그대로 참고합니다.
            on_off_lst[j] = (on_off_lst[j] + 1) % 2                     # 그냥 1 더하고 2로 나눈 나머지로 연산했습니다.

    else:                                                               # 여학생의 경우

        chk = stu_lst[i][1] - 1                                         # 시작 위치를 먼저 잡음, 인덱스 시작이 0번이므로 주의!
        on_off_lst[chk] = (on_off_lst[chk] + 1) % 2                     # 일단 시작 위치의 스위치는 무조건 바꿔 줌

        for j in range(1, min(n - chk, chk + 1)):                       # 중요 : 시작 위치에서 벽에 더 가까운 쪽까지의 거리를 재서 그 횟수만큼만 루프!
            if on_off_lst[chk + j] != on_off_lst[chk - j]:              # 같은 거리만큼 떨어진 스위치의 on/off가 서로 다르면 루프 탈출
                break
            else:                                                       # 스위치 상태가 서로 동일하다면
                on_off_lst[chk + j] = (on_off_lst[chk + j] + 1) % 2     # 시작 위치에서 같은 거리만큼 떨어진 2개의 스위치를 동시에 바꿈
                on_off_lst[chk - j] = (on_off_lst[chk - j] + 1) % 2

for i in range(0, n, 20):                                               # 왜!!!!!! 대체!!!!!!! 20개씩!!!!!!!! 끊어서!!!!!!! 출력을!!!!!!!!!
    print(*on_off_lst[i: i+20])                                         # for문의 step과 인덱스 슬라이싱을 활용해서 출력