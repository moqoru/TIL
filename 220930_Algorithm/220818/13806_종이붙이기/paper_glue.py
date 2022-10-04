import sys
sys.stdin = open('sample_input.txt')

# 스택을 2차원 리스트로 담을 경우 시간초과, 2개의 리스트로 변경
t = int(input())
for cs in range(t):
    n = int(input())
    stack_p, stack_m = [], []                           # 배치 방법, 남은 공간을 각각 담을 스택
    cnt = 0                                             # 배치 경우의 수 기록
    # 배치 방법은 10짜리를 세로로 놓는 경우를 1, 20짜리 하나를 놓는 경우를 2, 10짜리를 가로로 2개 놓는 경우를 3이라고 함

    stack_p += [1]                                      # 일단 10짜리 하나를 세로로 놓은 경우를 스택에 저장
    stack_m += [n - 10]

    if n > 10:                                          # 여백이 20 이상 남아있다면
        stack_p += [2, 3]                               # 20짜리를 넣은 경우와, 10짜리를 가로로 2개 넣은 경우도 저장
        stack_m += [n - 20, n - 20]

    while len(stack_p) > 0:                             # 스택이 빌 때까지 루프
        place, margin = stack_p.pop(), stack_m.pop()    # 맨 앞에 있는 걸 꺼내서
        if margin == 0:                                 # 여백 없이 꽉 찼다면
            cnt += 1                                    # 배치 경우의 수 1 증가
        else:                                           # 여백이 아직 더 남았다면
            stack_p += [1]                              # 먼저 10짜리를 세로로 놓은 경우를 각 스택에 저장
            stack_m += [margin - 10]
            if margin > 10:                             # 여백이 20 이상 남았다면
                stack_p += [2, 3]                       # 20짜리를 넣은 경우와, 10짜리를 가로로 2개 넣은 경우도 저장
                stack_m += [margin - 20, margin - 20]

    print(f'#{cs + 1} {cnt}')                           # 루프를 다 돌면 모든 경우 탐색이 끝난 것임