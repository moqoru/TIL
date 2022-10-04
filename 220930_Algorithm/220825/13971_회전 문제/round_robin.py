import sys
sys.stdin = open('sample_input.txt')

from collections import deque
t = int(input())

for cs in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))

    for i in range(m % n):                  # 한 바퀴가 n회이므로 m을 n으로 나눈 나머지만큼 돌리면 결과는 어차피 동일
        cur = q.popleft()                   # dequeue와 enqueue를 반복
        q.append(cur)

    print(f'#{cs + 1} {q[0]}')              # 맨 앞 숫자 출력