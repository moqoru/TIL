import sys
sys.stdin = open('sample_input(1).txt')

t = int(input())

for cs in range(t):
    n, m = map(int, input().split())                        # n : 판의 한 변 길이, m : 회문의 길이

    lst = [input() for _ in range(n)]
    lst_trans = list(zip(*lst))                             # 세로방향으로도 봐야 하므로 전치 행렬을 하나 만들어둠,
                                                            # 이때 zip은 결과값이 튜플이므로 주의!

    for i in range(n):                                      # 리스트를 한 줄 씩 탐색
        for j in range(n - m + 1):                          # 한 줄 안에서 리스트 길이 - 회문 길이만큼 탐색

            pal_chk = lst[i][j: j+m]                        # 회문의 길이만큼 자름
            pal_tr_chk = ''.join(lst_trans[i][j: j+m])      # 전치 행렬에서도 똑같이 하지만, 튜플이라서 문자열 변환 필요

            if pal_chk == pal_chk[::-1]:                    # 뒤집어도 같으면 회문이므로...
                pal = pal_chk                               # 회문을 저장
            if pal_tr_chk == pal_tr_chk[::-1]:              # 전치 행렬에서도 검사
                pal = pal_tr_chk

    print(f'#{cs + 1} {pal}')