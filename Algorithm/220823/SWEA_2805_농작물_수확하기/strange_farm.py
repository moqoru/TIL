import sys
sys.stdin = open('input.txt')

t = int(input())
for cs in range(t):

    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]
    half = n // 2                                       # 농장 길이의 절반, 마름모 영역 계산할 때 사용
    sum = 0

    for i in range(half + 1):                           # 마름모의 위쪽 절반 부분
        for j in range(half - i, n - half + i):
            sum += lst[i][j]
    
    for i in range(half + 1, n):                        # 마름모의 아래쪽 절반 부분
        for j in range(i - half, n - i + half):
            sum += lst[i][j]

    print(f'#{cs + 1} {sum}')