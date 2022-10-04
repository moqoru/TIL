import sys
sys.stdin = open('input.txt')

def s(num, div):
    cnt = 0
    while num % div == 0:       # 원래 숫자를 div로 나눌 수 있을 때까지 루프
        num //= div             # 원래 숫자를 div로 한번 나누고
        cnt += 1                # 나눈 횟수를 cnt에 저장
    return cnt                  # 나눈 횟수를 리턴

t = int(input())
for cs in range(t):
    n = int(input())
    print(f'#{cs + 1} {s(n, 2)} {s(n, 3)} {s(n, 5)} {s(n, 7)} {s(n, 11)}')
                                # n을 2, 3, 5, 7, 11으로 나눈 횟수를 함수로 호출해서 출력