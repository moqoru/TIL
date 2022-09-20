import sys
sys.stdin = open("input.txt")

ofl_chk = 0.5 ** 20 # 이 값이 13이면 될 거 같지만, 실제로는 훨씬 작아야 했다...
t = int(input()) # 사실 저 값은 우리가 직관적으로 정할 수 없다. 파이썬을 까봐야 알 듯.
for cs in range(t):
    n = float(input())
    now_num = 1.0
    ans = ""
    for i in range(12):
        now_num /= 2
        if n - now_num >= - ofl_chk:
            n -= now_num
            ans += "1"
            if n < ofl_chk:
                break
        else:
            ans += "0"
    if n >= ofl_chk:
        print(f'#{cs + 1} overflow')
    else:
        print(f'#{cs + 1} {ans}')