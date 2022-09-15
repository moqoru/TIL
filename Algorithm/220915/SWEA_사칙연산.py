import sys
sys.stdin = open('input.txt')

def postorder(cur):                         # 후위 순회로 검색
    if lst_l[cur] != 0:                     # 연산자라면 = 자식 노드가 있다면
        postorder(lst_l[cur])               # 먼저 좌, 우 노드를 모두 탐색 후...
        postorder(lst_r[cur])
        b = stk.pop()                       # 2개의 숫자를 스택에서 뽑음
        a = stk.pop()
        if lst_m[cur] == '+':               # 연산자에 따라 연산 처리 후 다시 스택에 저장
            stk.append(a + b)
        elif lst_m[cur] == '-':
            stk.append(a - b)
        elif lst_m[cur] == '*':
            stk.append(a * b)
        else:
            stk.append(a // b)
    else:                                   # 숫자라면
        stk.append(lst_m[cur])              # 그 위치의 숫자를 스택에 저장

for cs in range(10):
    n = int(input())
    lst_m, lst_l, lst_r = [0], [0], [0]
    stk = []
    for i in range(n):
        tup = input().split()
        if tup[1] in ['+', '-', '*', '/']:  # 연산자라면 입력 변수가 4개이므로
            lst_m.append(tup[1])            # 본인 노드, 좌우 자식 노드를 기록
            lst_l.append(int(tup[2]))
            lst_r.append(int(tup[3]))

        else:                               # 숫자라면 본인 노드를 기록 후, 자식 노드는 없다는 뜻으로 0을 기록
            lst_m.append(int(tup[1]))
            lst_l.append(0)
            lst_r.append(0)
    postorder(1)
    print(f'#{cs + 1} {stk[-1]}')           # 전부 완벽하게 수행됐다면 스택에는 최종 결과 숫자 하나만 들어있을 것
