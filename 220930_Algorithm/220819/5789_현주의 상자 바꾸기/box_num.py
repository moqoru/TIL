import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for cs in range(t):
    n, q = map(int, input().split())
    lst = [0] * n                           # 이번에는 상자 개수는 n이지만 0번부터 n-1까지 생성하도록 함

    for i in range(1, q + 1):               # i는 상자에 적을 값이 됨
        l, r = map(int, input().split())
        for j in range(l - 1, r):           # 왼쪽부터 오른쪽까지 루프하지만 시작이 0번이므로 -1씩 밀어서 적어줌
            lst[j] = i                      # 범위 내의 상자에 i를 기록

    print(f'#{cs + 1}', end = ' ')
    print(*lst)                             # 시작을 굳이 0번 상자로 한건 *lst를 쓰기 위함이었음...
