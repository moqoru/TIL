# n = 수의 갯수, m = 더하는 횟수, k = 한 개 숫자 연속 사용 최대 횟수
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
divk = m // (k + 1)
modk = m % (k + 1)
ans = lst[-1] * k * divk + lst[-1] * modk + lst[-2] * divk
print(ans)