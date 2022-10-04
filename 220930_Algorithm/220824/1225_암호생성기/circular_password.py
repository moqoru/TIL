import sys
sys.stdin = open('input.txt')

from collections import deque               # 데크 자료형을 쓰기 위해 import

for cs in range(10):
    t = int(input())
    q = deque(map(int, input().split()))    # 처음 입력부터 바로 데크 형태로 받을 수 있음

    bbaegi = 0                              # 빼기 작업을 해줄 숫자
    flag = True                             # 루프문 탈출 조건
    while flag:
        bbaegi += 1                         # 뺄 숫자는 1 - 2 - 3 - 4 - 5 순서대로 늘어남
        if bbaegi > 5:                      # 5 다음에는 1이 되어야 하므로 보정해 줌
            bbaegi = 1
        cur = q.popleft()                   # 큐에서 값을 하나 dequeue해 줌
        if cur - bbaegi <= 0:               # 빼기 작업을 했을 때 0 이하(0 포함!)가 되었다면
            q.append(0)                     # 0을 enqueue하고 break되게 처리
            flag = False
        else:                               # 아니라면 dequeue된 값에서 빼기 작업을 하고 다시 enqueue
            q.append(cur - bbaegi)

    print(f'#{t}', end=' ')
    print(*q)                               # 큐 자료형도 리스트처럼 *list 출력이 가능함
    # for i in range(len(q)):               # len()과 인덱스[] 연산도 모두 가능
    #     print(q[i], end=' ')              # 단 슬라이싱[ : ] 작업은 불가능함
    # print()