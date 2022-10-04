import sys
sys.stdin = open('input.txt')

t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    ans = "ON"
    # 2씩 계속 나머지 연산하는 것은 가장 오른쪽 비트부터 역순으로 자릿값을 구하는 것이니, n번 모두 1이 나오면 끝!
    for i in range(n):
        now_bit = m % 2
        m //= 2
        if not now_bit:
            ans = "OFF"
            break
    print(f'#{cs + 1} {ans}')
