import sys
sys.stdin = open("input.txt")

# 핵심 1 : 모든 코드의 마지막 비트는 1로 끝난다는 점을 적극 이용!
# 핵심 2 : 1이 들어있는 줄 한 줄만 체크하면 나머지 입력 리스트는 무시할 수 있음
# 먼저 리스트를 한 줄씩 체크해서 1이 있는지 확인, 1이 있는 리스트만 한 줄 잘라서 체크하고 끝냄
# 자른 한 줄짜리 리스트를 역순으로 바꿔서 1이 있는 위치를 기준으로 56칸만 자른 후, 다시 뒤집어서 연산하면 된다.

def num_chk(cod):                                               # 7개씩 자른 2진 숫자를 10진수 숫자로 변환
    if cod[1] == 1:                                             # 3, 4, 5, 6, 7, 8
        if cod[2] == 0:                                         # 4, 6
            if cod[3] == 0:
                return 4
            else:
                return 6
        elif cod[3] == 0:                                       # 5, 8
            if cod[4] == 0:
                return 5
            else:
                return 8
        else:                                                   # 3, 7
            if cod[4] == 1:
                return 3
            else:
                return 7
    elif cod[2] == 1:                                           # 1, 2
        if cod[3] == 1:
            return 1
        else:
            return 2
    else:                                                       # 0, 9
        if cod[4] == 1:
            return 0
        else:
            return 9

t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    lst = [list(map(int, input())) for _ in range(n)]           # 일단 입력 자체는 다 받아야 함...

    chk_byte, sum_byte = 0, 0
    for i in range(n):

        if 1 in lst[i]:                                         # 1이 있는 리스트만 체크
            rev_lst = lst[i][::-1]                              # 우선 뒤집고, 1이 맨 처음 나온 위치를 기준으로 56칸 만큼 슬라이싱
            start = rev_lst.index(1)                            # (.index는 값이 없으면 에러가 남)
            rev_cut = list(reversed(rev_lst[start: start+56]))  # reversed는 리턴된 자료형이 list가 아니라서 추가 변환 필요

            for j in range(0, 56, 7):                           # 7칸씩 다시 슬라이싱해서 그 위치의 숫자가 무엇인지 체크
                now_byte = num_chk(rev_cut[j: j+7])             # 함수로 체크해서 리턴값을 받아옴
                sum_byte += now_byte
                if not j % 2:                                   # 자릿수가 홀수일 경우
                    chk_byte += now_byte * 3
                else:                                           # 짝수일 경우
                    chk_byte += now_byte

            break                                               # 한 줄만 체크하면 땡이므로 바로 탈출

    if not chk_byte % 10:                                       # 유효한 코드일 때만 그 값을 출력
        print(f'#{cs + 1} {sum_byte}')
    else:
        print(f'#{cs + 1} 0')

