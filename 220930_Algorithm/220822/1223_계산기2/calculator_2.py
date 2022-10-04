import sys
sys.stdin = open('input.txt')

isp = {'*': 2, '/': 2, '-': 1, '+': 1, '(': 0}
icp = {'*': 2, '/': 2, '-': 1, '+': 1, '(': 3}

for cs in range(10):
    n = int(input())
    infix = input()

    stack = []
    postfix = []

    for token in infix:

        # 숫자가 들어오면 그냥 바로 결과 리스트에 붙임
        if token.isdecimal():
            postfix.append(token)

        # 추가 노트 : '('는 스택에는 무조건 들어감, 들어 있으면 다른 연산자는 무조건 위에 붙고, ')'가 나타날 때만 빠져나옴

        # 연산자라면...
        else:

            # 스택에 들어있는 게 있다면
            if stack:

                # 만약 ')' 연산자가 들어왔다면
                if token == ')':

                    # '('가 나올 때까지 스택에서 뽑고 결과 리스트에 붙임, '(' 자체는 결과 리스트에 붙지 않음
                    tmp = stack.pop()
                    while tmp != '(':
                        postfix.append(tmp)
                        tmp = stack.pop()

                # 새로 들어올 연산자가 스택 끝의 연산자보다 우선순위가 높으면
                elif icp[token] > isp[stack[-1]]:

                    # 스택에 바로 넣음
                    stack.append(token)

                # 새로 들어올 연산자가 스택 끝의 연산자보다 우선순위가 낮으면
                else:

                    # 스택에 남아있는 연산자가 새로 들어올 연산자보다 우선순위 높아질 때까지 스택에서 계속 빼내서 결과 리스트에 붙임
                    while stack and icp[token] <= isp[stack[-1]]:
                        postfix.append(stack.pop())

                    # 그런 뒤 새로 들어올 연산자를 스택에 삽입
                    stack.append(token)

            # 스택이 비어있으면 그냥 연산자를 바로 스택에 넣기
            else:
                stack.append(token)

    # 남은 스택은 역순으로 결과 리스트에 붙이면 끝 (하나씩 pop 해서 append 하는 것과 동일)
    postfix.extend(stack[::-1])
    stack = []

    # 후위 표기법으로 저장된 결과 리스트에서 연산
    for token in postfix:

        # 값이 숫자라면 스택에 숫자로 바꿔 저장
        if token.isdecimal():
            stack.append(int(token))

        # 기호라면 스택에서 숫자 2개를 뽑아 연산하고 다시 스택에 저장
        else:
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '*':
                stack.append(a * b)

    # 맨 마지막에는 스택에 결과 값 하나만 남음
    print(f'#{cs + 1} {stack[-1]}')
