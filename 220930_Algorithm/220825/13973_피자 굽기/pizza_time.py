import sys
sys.stdin = open('sample_input(2).txt')

from collections import deque

t = int(input())
for cs in range(t):

    n, m = map(int, input().split())
    lst = [0] + list(map(int, input().split()))             # 피자 번호가 1번부터 시작이므로 0번 인덱스는 더미로 채워줌
    q_cheeze, q_num = deque(), deque()                      # 각각 피자의 치즈 정보, 피자의 번호를 저장할 큐
    cnt, cur_num = 1, -1                                    # cnt는 화덕에 넣을 피자 번호, cur_num은 현재 화덕 1번칸에 보이는 피자 번호

    while cnt <= n:                                         # 화덕의 공간만큼 피자를 먼저 넣기
        q_cheeze.append(lst[cnt])                           # 2개의 큐에 피자의 치즈 정보와 피자 번호 넣음
        q_num.append(cnt)
        cnt += 1                                            # 다음번에 넣을 피자 번호 갱신

    while q_cheeze:                                         # 큐 = 화덕에 피자가 남아 있는 동안 루프
        cur_cheeze = q_cheeze.popleft() // 2                # 큐에서 피자를 꺼냄, 한 바퀴 돈 이후이므로 절반만큼 치즈가 녹은 상태
        cur_num = q_num.popleft()                           # 큐에서 피자 번호도 꺼냄

        if cur_cheeze != 0:                                 # 치즈가 덜 녹았다면 다시 enqueue
            q_cheeze.append(cur_cheeze)
            q_num.append(cur_num)

        elif cnt <= m:                                      # 피자를 꺼내야 하는데 아직 남은 피자가 있다면
            q_cheeze.append(lst[cnt])                       # 그 다음 번호의 피자를 enqueue
            q_num.append(cnt)
            cnt += 1                                        # 피자 번호 갱신
                                                            # 남은 피자가 없다면 enqueue 없이 dequeue만 진행하다가 큐가 비어서 루프 종료
    print(f'#{cs + 1} {cur_num}')                           # 마지막으로 꺼낸 피자 번호를 저장했다가 출력