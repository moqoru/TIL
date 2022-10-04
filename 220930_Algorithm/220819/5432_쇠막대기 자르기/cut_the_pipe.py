import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for cs in range(t):

    lst = input()                       # 한개의 긴 문자열로 입력받음
    stack = []                          # 막대기의 시작점만 저장할 스택
    cnt = 0                             # 막대기 조각 갯수
    laser = False                       # 레이저 발사 여부 체크

    for i in lst:

        if i == '(':                    # <막대기 쌓기 단계>

            stack.append(i)             # 스택에 저장하여 현재 겹쳐있는 막대기 개수를 늘림
            laser = True                # 바로 다음에 ')'가 나오면 레이저를 쏠 수 있도록 레이저 전원을 켬

        else:                           # <레이저 쏘기 or 막대기 빼기 단계>

            stack.pop()                 # 막대기가 끝나는 건지 레이저 쏘는 건지는 모르므로 일단 pop

            if laser:                   # '(' 직후에 ')'이면 레이저 발사
                cnt += len(stack)       # 현재 겹쳐진 막대기 갯수만큼 조각이 늘어남
                laser = False           # 이후에 ')'가 또 나오면 그건 막대기가 끝나는 것이므로 레이저 전원을 꺼둠

            else:                       # 레이저 전원이 꺼져 있다면
                cnt += 1                # 막대기 1개가 끝났다는 의미이므로 조각 1개만 추가

    print(f'#{cs + 1} {cnt}')