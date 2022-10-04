import sys
sys.stdin = open('sample_input(2).txt')

t = int(input())

for cs in range(t):

    str1 = input()                                  # str1이 찾으려는 key 문자 집합, str2가 원본 문자열
    str2 = input()

    max_str = 0                                     # 가장 많이 나온 글자의 횟수
    for i in str1:                                  # key 문자 집합에서 찾을 글자를 하나씩 고름
        cnt = 0                                     # 이번 글자가 나온 횟수

        for j in str2:                              # 원본 문자열을 한 글자씩 탐색
            if i == j:                              # 글자가 일치하면 횟수 1씩 증가
                cnt += 1

        if max_str < cnt:                           # 가장 많이 나온 글자의 횟수를 갱신
            max_str = cnt

    print(f'#{cs + 1} {max_str}')