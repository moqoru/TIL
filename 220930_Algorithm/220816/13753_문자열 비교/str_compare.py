import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for cs in range(t):

    str1 = input()                          # 찾을 문자열
    str2 = input()                          # 뒤져볼 문자열
    n, m = len(str1), len(str2)             # 각 문자열의 길이
    cnt = 0                                 # 찾았는지 여부 저장

    for i in range(m - n + 1):              # 뒤져볼 문자열에서 찾을 문자열의 길이만큼 빼고 탐색
        if str1 == str2[i: i + n]:          # 찾을 문자열 길이만큼 잘랐을 때 똑같으면
            cnt = 1                         # 찾았다고 기록하고 탈출
            break

    print(f'#{cs + 1} {cnt}')
