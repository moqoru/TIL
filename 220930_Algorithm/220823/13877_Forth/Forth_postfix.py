import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for cs in range(t):
    postfix = input().split()

    stack = []                                          # 계산하기 위한 숫자만 임시저장할 스택
    error = False                                       # 에러 여부 체크
    ans = 0                                             # 답 출력 변수

    for idx, token in enumerate(postfix):

        if token.isdecimal():                           # 뽑은 값이 숫자라면
            stack.append(int(token))                    # 스택에 저장

        else:
            
            if idx == len(postfix)-1 and token == '.':  # 마지막 위치의 종료 연산자라면
                ans = stack.pop()                       # 마지막에 스택에 든 값이 결과값
                continue
                
            elif len(stack) < 2:                        # 스택의 숫자 개수가 부족하다면 = 연산자에 비해 숫자 개수가 부족하다면
                error = True                            # 에러 발생, 루프 즉시 중단
                break

            b = stack.pop()                             # 연산용 숫자 2개를 스택에서 뽑음
            a = stack.pop()                             # 스택은 후입선출이므로 연산할 숫자의 순서가 반대로 나온다!

            if token == '+':                            # 연산자 종류에 맞게 연산 후 그 숫자를 스택에 저장
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
            else:                                       # 종료 연산자가 일찍 나오거나 한 경우라면
                error = True
                break

    if stack or error:                                  # 에러가 났거나 스택이 비어있지 않다면 = 숫자 갯수가 연산자에 비해 많다면
        print(f'#{cs + 1} error')                       # 에러 발생으로 출력

    else:                                               # 정상적으로 종료한 경우 결과값 출력
        print(f'#{cs + 1} {ans}')
