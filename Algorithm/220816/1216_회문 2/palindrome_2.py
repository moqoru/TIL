import sys
sys.stdin = open('input.txt')

for cs in range(10):

    t = int(input())
    lst = [input() for _ in range(100)]
    lst_trans = list(zip(*lst))                                 # 전치 행렬을 만들어 둠, 세로방향 탐색용
    cnt = 0
    for k in range(100, 0, -1):                                 # 회문의 길이, 긴 것부터 짧은 것 순서대로 탐색
        for i in range(100):                                    # 탐색할 리스트의 행
            for j in range(100 - k + 1):                        # 회문의 시작점의 열
                lst_str = ''.join(lst[i][j:j+k])                # 문자열을 가로열, 세로열 각각 join으로 합쳐줌
                lst_trans_str = ''.join(lst_trans[i][j:j+k])    # 문자열 리스트는 [::-1]이 바로 적용되지 않으므로 join 필수
                if (lst_str == lst_str[::-1] or \
                    lst_trans_str == lst_trans_str[::-1]) and \
                    cnt < k:                                    # 가로/세로열에서 회문을 처음 찾은 경우
                    cnt = k                                     # 회문 길이 저장
                    break
            if cnt != 0:                                        # 회문을 찾은 경우 더이상 탐색하지 않고 break
                break
        if cnt != 0:
            break
    print(f'#{t} {cnt}')
