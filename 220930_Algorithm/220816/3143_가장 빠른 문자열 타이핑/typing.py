import sys
sys.stdin = open('sample_input.txt')
t = int(input())

for cs in range(t):
    # index slicing 없이 구현?
    a, b = input().split()
    i, j, cnt = 0, 0, 0                     # j : b 문자열 탐색, cnt : 키 입력 횟수

    while i < len(a):                       # a 문자열을 끝까지 탐색할 때까지 반복

        cur = a[i]                          # cur는 a 문자열에서 탐색 시작할 부분의 문자열

        if cur == b[j]:                     # cur가 b 문자열의 시작 부분과 똑같다면
            j += 1                          # j를 늘려 b 문자열과 동일한지 한 칸씩 탐색하게 함

            if j == len(b):                 # b 문자열과 완전히 동일한지 판별이 끝나면
                cnt += 1                    # 키를 b 문자열 1번만 누르면 되므로 cnt에 1만 더함
                j = 0                       # b 문자열을 다시 탐색할 수 있도록 j를 리셋

        elif cur != b[j] and j != 0:        # b 문자열과 동일한 부분이 있는 줄 알았는데 아니었다면
            cnt += 1                        # 원래 탐색하던 위치로 되돌아가서 다음 칸에서 시작해야 하므로, 1만 증가
            i -= j                          # i의 위치를 지금까지 탐색한 만큼 되돌림
            j = 0                           # b 문자열을 다시 탐색할 수 있도록 j를 리셋

        else:                               # 아무것도 안 겹치면 그냥 자판을 정직하게 1번 눌러야 하므로
            cnt += 1                        # cnt를 1 늘려줌

        i += 1                              # i를 다음 칸으로 옮김

    cnt += j                                # b 탐색하는 중간에 a 문자열이 끝나는 경우가 있으므로,
    print(f'#{cs + 1} {cnt}')               # 마지막에 cnt를 그만큼 추가로 늘려줌