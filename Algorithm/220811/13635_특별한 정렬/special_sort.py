import sys
sys.stdin = open('sample_input(3).txt')

t = int(input())

for cs in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    print(f'#{cs + 1}', end='')                     # 이번 경우는 계산 중에 출력이 이어지므로 case 번호 먼저 출력
    for i in range(10):                             # 10개 까지만 출력
        a = max(lst) if i % 2 == 0 else min(lst)    # 짝수번째 (0, 2, ...)라면 최대값, 홀수번째라면 최소값 추출
        lst.remove(a)                               # 추출한 값은 리스트에서 제거
        print(f' {a}', end='')                      # 추출한 값을 한 줄 안에서 하나씩 출력
    print()                                         # 다 나왔다면 줄 바꿈